"""Train, calibrate, validate and query a supervised five-session price model."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import uuid
from datetime import datetime, timezone, timedelta

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier, HistGradientBoostingRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, brier_score_loss, log_loss, mean_absolute_error, roc_auc_score
from sklearn.model_selection import TimeSeriesSplit
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import StandardScaler
from threadpoolctl import threadpool_limits

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.features.price_learning_dataset import (
    FEATURES, FEATURE_VERSION, build_dataset, load_snapshots, make_features,
    normalize_code, temporal_partitions,
)

PROBABILITY_THRESHOLD = 0.60
MIN_TEST_DATES = 20


def json_text(value):
    return json.dumps(value, ensure_ascii=False, indent=2, default=str, allow_nan=False)


def classifiers():
    return {
        "logistic_regression": make_pipeline(StandardScaler(), LogisticRegression(C=0.3, solver="liblinear", max_iter=1000, random_state=42)),
        "hist_gradient_boosting": HistGradientBoostingClassifier(
            max_iter=100, max_leaf_nodes=7, max_depth=3, min_samples_leaf=80,
            l2_regularization=10, learning_rate=0.05, early_stopping=False, random_state=42,
        ),
    }


def date_weights(frame):
    if frame.empty or frame['signal_date'].isna().any():
        raise ValueError('Date weights require nonempty dated observations.')
    counts = frame.groupby('signal_date')['signal_date'].transform('size').to_numpy(dtype=float)
    weights = 1.0 / counts
    return weights / weights.mean()


def fit_estimator(model, features, target, weights=None):
    if weights is None:
        return model.fit(features, target)
    if isinstance(model, Pipeline):
        return model.fit(features, target, **{name + '__sample_weight': weights for name in model.named_steps})
    return model.fit(features, target, sample_weight=weights)


def new_regressor():
    return HistGradientBoostingRegressor(
        loss='absolute_error', max_iter=100, max_leaf_nodes=7, min_samples_leaf=80,
        l2_regularization=10, early_stopping=False, learning_rate=0.05, random_state=42,
    )


def choose_classifier(train, features=None, date_balanced=False):
    """Select only inside training history; validation and test labels are untouched."""
    features = FEATURES if features is None else features
    days = np.array(sorted(train["signal_date"].unique()))
    scores = {}
    for name, model in classifiers().items():
        folds = []
        for train_indices, validation_indices in TimeSeriesSplit(n_splits=3).split(days):
            validation_start = pd.Timestamp(days[validation_indices[0]])
            fitting = train[train["signal_date"].isin(days[train_indices]) & (train["label_available_date"] < validation_start)]
            validation = train[train["signal_date"].isin(days[validation_indices])]
            if len(fitting) < 100 or fitting["target"].nunique() < 2 or validation.empty:
                continue
            fit_estimator(model, fitting[features], fitting['target'], date_weights(fitting) if date_balanced else None)
            folds.append(float(log_loss(validation["target"], model.predict_proba(validation[features]), labels=[0, 1],
                                       sample_weight=date_weights(validation) if date_balanced else None)))
        if len(folds) >= 2:
            scores[name] = {"mean_log_loss": float(np.mean(folds)), "fold_log_losses": folds}
    if not scores:
        raise ValueError("Not enough mature outcomes for at least two purged training folds.")
    winner = min(scores, key=lambda name: scores[name]["mean_log_loss"])
    model = classifiers()[winner]
    fit_estimator(model, train[features], train['target'], date_weights(train) if date_balanced else None)
    return winner, model, scores


def logits(model, features):
    probability = np.clip(model.predict_proba(features)[:, 1], 1e-6, 1 - 1e-6)
    return np.log(probability / (1 - probability)).reshape(-1, 1)


def predict_values(bundle, features):
    probability = bundle["calibrator"].predict_proba(logits(bundle["classifier"], features))[:, 1]
    expected_return = bundle["regressor"].predict(features)
    return probability, expected_return


def block_bootstrap_lower(daily_returns):
    """Resample five-day blocks, not individual correlated stock predictions."""
    values = np.asarray(daily_returns, dtype=float)
    if len(values) < MIN_TEST_DATES:
        return None
    rng = np.random.default_rng(42)
    samples = []
    block = 5
    for _ in range(1000):
        starts = rng.integers(0, len(values), size=int(np.ceil(len(values) / block)))
        indices = np.concatenate([(np.arange(start, start + block) % len(values)) for start in starts])[:len(values)]
        samples.append(values[indices].mean())
    return float(np.quantile(samples, 0.025))


def validation_summary(test, probability, expected_return, baseline_probability, cost):
    result = test[["stock_code", "signal_date", "target_date", "label_available_date", "target", "target_return", "net_return_proxy"]].copy()
    result["probability_above_cost"] = probability
    result["predicted_close_return"] = expected_return
    result["selected_by_fixed_policy"] = (probability >= PROBABILITY_THRESHOLD) & (expected_return > cost)
    selected = result[result["selected_by_fixed_policy"]]
    daily = selected.groupby("signal_date")["net_return_proxy"].mean()
    summary = {
        "evaluated_rows": len(result), "signal_dates": int(result["signal_date"].nunique()),
        "base_rate": float(test["target"].mean()),
        "accuracy_at_half": float((test["target"].to_numpy() == (probability >= 0.5)).mean()),
        "majority_class_accuracy": float(max(test["target"].mean(), 1 - test["target"].mean())),
        "balanced_accuracy": float(balanced_accuracy_score(test["target"], probability >= 0.5)),
        "roc_auc": float(roc_auc_score(test["target"], probability)),
        "brier_score": float(brier_score_loss(test["target"], probability)),
        "baseline_brier_score": float(brier_score_loss(test["target"], np.full(len(test), baseline_probability))),
        "return_mae": float(mean_absolute_error(test["target_return"], expected_return)),
        "selected_count": len(selected), "selected_dates": int(len(daily)),
        "selected_success_rate": float(selected["target"].mean()) if len(selected) else None,
        "selected_mean_net_return_proxy": float(selected["net_return_proxy"].mean()) if len(selected) else None,
        "selected_daily_mean_net_return_proxy": float(daily.mean()) if len(daily) else None,
        "selected_daily_return_lower_95": block_bootstrap_lower(daily.to_numpy()),
    }
    reasons = []
    if summary["signal_dates"] < MIN_TEST_DATES:
        reasons.append("fewer_than_20_test_signal_dates")
    if len(selected) < 100 or len(daily) < MIN_TEST_DATES:
        reasons.append("insufficient_fixed_policy_selection_history")
    if summary["roc_auc"] < 0.52:
        reasons.append("weak_out_of_time_discrimination")
    if summary["brier_score"] >= summary["baseline_brier_score"]:
        reasons.append("probabilities_do_not_beat_constant_baseline")
    if summary["selected_success_rate"] is None or summary["selected_success_rate"] < summary["base_rate"] + 0.03:
        reasons.append("selected_precision_lift_below_3_percentage_points")
    if summary["selected_daily_return_lower_95"] is None or summary["selected_daily_return_lower_95"] <= 0:
        reasons.append("positive_daily_return_edge_not_established")
    summary["recommendation_gate_passed"] = not reasons
    summary["gate_reasons"] = reasons
    return summary, result


def train_model(data_root, output_dir, as_of, horizon=5, cost=0.003, source_ref="local", calibration_start=None, test_start=None):
    snapshots, source_metadata = load_snapshots(data_root)
    dataset, metadata = build_dataset(snapshots, horizon=horizon, cost=cost, as_of=as_of)
    train, calibration, test = temporal_partitions(dataset, calibration_start, test_start)
    with threadpool_limits(limits=2):
        name, classifier, cv_scores = choose_classifier(train)
        calibrator = LogisticRegression(C=1.0, solver="liblinear", max_iter=1000, random_state=42)
        calibrator.fit(logits(classifier, calibration[FEATURES]), calibration["target"])
        regressor = new_regressor()
        regressor.fit(train[FEATURES], train["target_return"])
        bundle = {"classifier": classifier, "calibrator": calibrator, "regressor": regressor}
        probability, expected_return = predict_values(bundle, test[FEATURES])
    summary, predictions = validation_summary(test, probability, expected_return, float(calibration["target"].mean()), cost)
    summary["baseline_return_mae"] = float(mean_absolute_error(test["target_return"], np.full(len(test), train["target_return"].median())))
    if summary["return_mae"] >= summary["baseline_return_mae"]:
        summary["gate_reasons"].append("return_forecast_does_not_beat_training_median")
        summary["recommendation_gate_passed"] = False
    provenance = metadata.get('history_provenance', {})
    if provenance.get('scope') == 'pilot':
        summary['gate_reasons'].append('pilot_universe_not_production_validated')
        summary['recommendation_gate_passed'] = False
    elif provenance:
        summary['gate_reasons'].append('reconstructed_history_requires_forward_validation')
        summary['recommendation_gate_passed'] = False
    summary["calibration_bins"] = []
    for lower, upper in [(0.0, 0.2), (0.2, 0.4), (0.4, 0.6), (0.6, 0.8), (0.8, 1.0)]:
        mask = (probability >= lower) & ((probability < upper) if upper < 1 else (probability <= upper))
        if mask.any():
            summary["calibration_bins"].append({"range": [lower, upper], "count": int(mask.sum()),
                "mean_probability": float(probability[mask].mean()), "observed_rate": float(test.loc[mask, "target"].mean())})
    fingerprint = hashlib.sha256(pd.util.hash_pandas_object(
        dataset[["stock_code", "signal_date", "label_available_date", "target_return"] + FEATURES], index=False
    ).values.tobytes()).hexdigest()
    metadata.update(source_metadata)
    metadata.update({
        "source_ref": source_ref, "dataset_sha256": fingerprint,
        "data_root": str(Path(data_root).resolve()),
        "trained_at": datetime.now(timezone.utc).isoformat(), "as_of": str(as_of),
        "classifier": name, "features": FEATURES, "training_cv": cv_scores,
        "baseline_probability": float(calibration['target'].mean()),
        "calibration_parameters": {"slope": float(calibrator.coef_[0, 0]), "intercept": float(calibrator.intercept_[0])},
        "fixed_temporal_boundaries": {"calibration_start": calibration_start, "test_start": test_start},
        "probability_threshold": PROBABILITY_THRESHOLD, "test": summary,
        "latest_signal_date": str(snapshots.loc[snapshots['signal_date'] <= pd.Timestamp(as_of), 'signal_date'].max().date()),
        "partitions": {
            label: {"rows": len(part), "start": str(part["signal_date"].min().date()),
                    "end": str(part["signal_date"].max().date()),
                    "positive_rate": float(part['target'].mean()),
                    "latest_label_available": str(part["label_available_date"].max().date())}
            for label, part in [("train", train), ("calibration", calibration), ("test", test)]
        },
    })
    bundle["metadata"] = metadata
    return save_artifacts(bundle, predictions, output_dir)


def save_artifacts(bundle, predictions, output_dir, predictions_name='holdout_predictions.csv'):
    if Path(predictions_name).name != predictions_name or not predictions_name.endswith('.csv'):
        raise ValueError('Predictions artifact must be a CSV filename.')
    metadata = bundle['metadata']
    fingerprint = metadata['dataset_sha256']
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "_" + fingerprint[:10] + "_" + uuid.uuid4().hex[:6]
    run_dir = output_dir / "runs" / run_id
    run_dir.parent.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(dir=run_dir.parent) as staging:
        staging = Path(staging)
        joblib.dump(bundle, staging / "model.joblib", compress=3)
        (staging / "validation.json").write_text(json_text(metadata) + "\n", encoding="utf-8")
        predictions.to_csv(staging / predictions_name, index=False)
        (staging / "report.md").write_text(render_report(metadata), encoding="utf-8")
        os.rename(staging, run_dir)
    with tempfile.NamedTemporaryFile(mode="w", dir=output_dir, delete=False, encoding="utf-8") as handle:
        json.dump({"run_id": run_id}, handle)
        pointer = handle.name
    os.replace(pointer, output_dir / "latest.json")
    return metadata, run_dir


def render_report(metadata):
    test = metadata["test"]
    lines = ["# Supervised Price Forecast Model", "", "Target: " + metadata["target_definition"],
             "", "Classifier: " + metadata["classifier"], "", "## Time-separated validation", "",
             "| Partition | Rows | Signal start | Signal end | Latest label available |", "|---|---:|---|---|---|"]
    for name, part in metadata["partitions"].items():
        lines.append(f"| {name} | {part['rows']} | {part['start']} | {part['end']} | {part['latest_label_available']} |")
    if metadata.get('asof_only'):
        lines += ['', 'Only labels available by the recorded as-of were used. Training labels crossing into calibration are purged. Future-month evaluation is stored separately, never attached as known validation to this bundle.',
                  '', '## Research Status (No Future Validation)', '', '| Metric | Value |', '|---|---:|']
    else:
        lines += ["", "Labels crossing the next partition boundary are purged. Classifier selection uses only purged expanding folds within training. Probability calibration uses only the middle period. Final test labels do not choose models or thresholds.",
                  "", "## Held-out results", "", "| Metric | Value |", "|---|---:|"]
    for key, value in test.items():
        if key not in {"gate_reasons", "calibration_bins"}:
            lines.append(f"| {key} | {value} |")
    if metadata.get('history_provenance'):
        lines += ['', 'History provenance: ' + json_text(metadata['history_provenance']), '']
    lines += ["", "Recommendation gate reasons: " + ", ".join(test["gate_reasons"]), "",
              "Probabilities are calibrated model estimates, not guaranteed hit rates. Return predictions are point estimates. Neither is the legacy dashboard Wilson score.",
              "", metadata["execution_note"], metadata["universe_note"], "",
              "Five-session outcomes and stocks on the same date overlap. Daily return uncertainty uses five-day block resampling; individual-stock sample counts are not independent trial counts.", "",
              "Source ref: " + metadata["source_ref"], "Dataset SHA256: " + metadata["dataset_sha256"], ""]
    return "\n".join(lines)


def load_bundle(output_dir):
    output_dir = Path(output_dir)
    run_id = json.loads((output_dir / "latest.json").read_text(encoding="utf-8"))["run_id"]
    if Path(run_id).name != run_id or not run_id:
        raise ValueError("Invalid model run identifier.")
    bundle = joblib.load(output_dir / "runs" / run_id / "model.joblib")
    from src.features.market_context import MARKET_FEATURE_VERSION
    if bundle["metadata"]["feature_version"] not in {FEATURE_VERSION, 'price_completed_history_v2', MARKET_FEATURE_VERSION}:
        raise ValueError("Model feature schema mismatch; retrain the model.")
    expected = FEATURES
    if bundle['metadata']['feature_version'] == MARKET_FEATURE_VERSION:
        from src.features.market_context import MARKET_FEATURES
        expected = FEATURES + MARKET_FEATURES
    if bundle['metadata']['features'] != expected:
        raise ValueError('Model feature columns do not match its declared schema.')
    return bundle


def load_model_snapshots(data_root, metadata):
    snapshots, source = load_snapshots(data_root)
    from src.features.market_context import MARKET_FEATURE_VERSION, add_market_context
    if metadata['feature_version'] == MARKET_FEATURE_VERSION:
        if snapshots.attrs.get('feature_version') != 'price_completed_history_v2':
            raise ValueError('Market-context inference requires coherent completed OHLCV history.')
        snapshots = add_market_context(snapshots, metadata['market_context']['min_stocks'])
    return snapshots, source


def stock_catalog(roots):
    catalog = {}
    for root in roots:
        root = Path(root)
        for folder, pattern in [("data/raw", "stock_market_lookup_*.csv"),
                                ("data/processed", "ml_stock_catalog.csv"),
                                ("data/processed", "price_based_candidates_*.csv"),
                                ("data/processed", "ml_dataset_*.csv")]:
            for path in sorted((root / folder).glob(pattern)):
                try:
                    frame = pd.read_csv(path, dtype={"stock_code": str}, usecols=lambda c: c in {"stock_code", "stock_name", "corp_name"})
                except (OSError, ValueError):
                    continue
                if "stock_code" not in frame:
                    continue
                for column in ["stock_name", "corp_name"]:
                    if column in frame:
                        for code, name in zip(frame["stock_code"], frame[column]):
                            if pd.notna(name) and str(name).strip():
                                catalog.setdefault(str(name).strip(), set()).add(normalize_code(code))
    return catalog


def resolve_stock(query, roots):
    query = str(query).strip()
    if len(query) == 6 and query.isascii() and query.isalnum():
        return normalize_code(query)
    matches = stock_catalog(roots).get(query, set())
    if len(matches) != 1:
        raise ValueError("종목명이 없거나 중복됩니다. 정확한 6자리 종목코드를 입력하세요: " + query)
    return next(iter(matches))


def forecast_row(bundle, row, as_of):
    metadata = bundle["metadata"]
    frame = pd.DataFrame([row])
    from src.features.market_context import model_features
    features = model_features(frame, metadata.get('features', FEATURES))
    if features.isna().any(axis=None) or features["volume_ratio_20d"].iloc[0] <= 0:
        raise ValueError("Prediction requires complete price features and positive volume.")
    signal_date = pd.Timestamp(row["signal_date"]).normalize()
    as_of = pd.Timestamp(as_of).normalize()
    if as_of < pd.Timestamp(metadata["as_of"]).normalize():
        raise ValueError("Historical inference cannot use a model trained with later data.")
    if signal_date > as_of:
        raise ValueError("Future-dated input is not allowed.")
    with threadpool_limits(limits=2):
        probability, expected_return = predict_values(bundle, features)
    if not np.isfinite(probability).all() or not np.isfinite(expected_return).all():
        raise ValueError("Non-finite model prediction.")
    stale = (as_of - signal_date).days > 7
    gate = metadata["test"]["recommendation_gate_passed"]
    recommend = gate and not stale and probability[0] >= metadata["probability_threshold"] and expected_return[0] > metadata["cost_assumption"]
    return {
        "stock_code": normalize_code(row["stock_code"]), "signal_date": str(signal_date.date()),
        "as_of": str(as_of.date()), "horizon_sessions": metadata["horizon_sessions"],
        "probability_above_cost": round(float(probability[0]), 6),
        "predicted_close_return": round(float(expected_return[0]), 6),
        "cost_assumption": metadata["cost_assumption"],
        "status": "STALE_DATA" if stale else ("VALIDATED" if gate else "RESEARCH_ONLY"),
        "recommendation": "MONITOR_CANDIDATE" if recommend else "ABSTAIN",
        "recommendation_ko": "관찰 후보" if recommend else "추천 보류",
        "validation_base_rate": metadata["test"]["base_rate"],
        "validation_auc": metadata["test"]["roc_auc"],
        "gate_reasons": metadata["test"]["gate_reasons"],
        "model_trained_at": metadata["trained_at"],
    }


def refreshed_signal(code, as_of, feature_version=FEATURE_VERSION):
    from src.features.market_context import MARKET_FEATURE_VERSION
    if feature_version == MARKET_FEATURE_VERSION:
        raise ValueError('Market-context models require matching completed universe data, not a single-stock --refresh. Update the full data-root first.')
    from src.crawler.kis_client import KISClient, KISCredentialsMissing
    from src.crawler.market_clock import completed_price_cutoff
    from src.features.daily_price_signals import calculate_signal
    # Only completed daily bars are used, even when the request is made intraday.
    end = min(pd.Timestamp(as_of), pd.Timestamp(completed_price_cutoff()))
    try:
        client = KISClient()
    except KISCredentialsMissing as error:
        raise ValueError("KIS_APP_KEY, KIS_APP_SECRET 설정이 필요합니다. 기존 스냅샷 조회는 --refresh 없이 실행하세요.") from error
    prices = client.get_daily_ohlcv(code, (end - pd.Timedelta(days=80)).strftime("%Y%m%d"), end.strftime("%Y%m%d"))
    if prices.empty or 'date' not in prices:
        raise ValueError('KIS did not return completed daily prices for this stock.')
    prices = prices[pd.to_datetime(prices['date']) <= end]
    if len(prices) < 21:
        raise ValueError("KIS did not return at least 21 completed daily bars.")
    from src.features.completed_price_dataset import HISTORY_FEATURE_VERSION, history_features
    if feature_version == HISTORY_FEATURE_VERSION:
        return history_features(prices).iloc[-1]
    return calculate_signal(prices, Path("kis_completed_daily_bars"))


def main():
    today = datetime.now(timezone(timedelta(hours=9))).date().isoformat()
    parser = argparse.ArgumentParser(description="학습 기반 5거래일 가격 예측 / Supervised price forecasting")
    parser.add_argument("command", choices=["train", "predict", "recommend"])
    parser.add_argument("--data-root", type=Path)
    parser.add_argument("--model-dir", type=Path, default=ROOT / "data/models/price_forecaster")
    parser.add_argument("--as-of", default=today)
    parser.add_argument("--source-ref", default="local")
    parser.add_argument("--calibration-start")
    parser.add_argument("--test-start")
    parser.add_argument("--stock")
    parser.add_argument("--report-path", type=Path)
    parser.add_argument("--output", type=Path, help="Save current stock predictions as CSV (recommend) or JSON (predict)")
    parser.add_argument("--refresh", action="store_true", help="Fetch completed daily bars from KIS for the requested stock")
    args = parser.parse_args()
    os.chdir(ROOT)
    try:
        if args.command == "train":
            metadata, run_dir = train_model(args.data_root or ROOT, args.model_dir, args.as_of, source_ref=args.source_ref,
                                            calibration_start=args.calibration_start, test_start=args.test_start)
            if args.report_path:
                args.report_path.parent.mkdir(parents=True, exist_ok=True)
                args.report_path.write_text(render_report(metadata), encoding="utf-8")
            print(json_text({"run_dir": run_dir, "classifier": metadata["classifier"], "partitions": metadata["partitions"], "test": metadata["test"]}))
            return
        bundle = load_bundle(args.model_dir)
        data_root = args.data_root or Path(bundle["metadata"].get("data_root", ROOT))
        as_of = pd.Timestamp(args.as_of).normalize()
        snapshots = pd.DataFrame()
        if not (args.command == "predict" and args.refresh):
            snapshots, _ = load_model_snapshots(data_root, bundle['metadata'])
            snapshots = snapshots[(snapshots["signal_date"] <= as_of) & (snapshots["snapshot_date"] <= as_of)]
        if args.command == "predict":
            if not args.stock:
                raise ValueError("predict requires --stock 종목명 또는 종목코드")
            code = resolve_stock(args.stock, [ROOT, data_root])
            if args.refresh:
                row = refreshed_signal(code, args.as_of, bundle['metadata']['feature_version'])
            else:
                matches = snapshots[snapshots["stock_code"] == code].sort_values("signal_date")
                if matches.empty:
                    raise ValueError("No price snapshot for this stock. Use --refresh with KIS credentials.")
                row = matches.iloc[-1]
            prediction = forecast_row(bundle, row, args.as_of)
            if args.output:
                args.output.parent.mkdir(parents=True, exist_ok=True)
                args.output.write_text(json_text(prediction) + "\n", encoding="utf-8")
            print(json_text(prediction))
        else:
            rows = []
            all_predictions = []
            for _, row in snapshots.sort_values("signal_date").drop_duplicates("stock_code", keep="last").iterrows():
                try:
                    prediction = forecast_row(bundle, row, args.as_of)
                    all_predictions.append(prediction)
                    if prediction["recommendation"] == "MONITOR_CANDIDATE":
                        rows.append(prediction)
                except ValueError:
                    continue
            rows.sort(key=lambda row: row["probability_above_cost"], reverse=True)
            if args.output:
                args.output.parent.mkdir(parents=True, exist_ok=True)
                pd.DataFrame(all_predictions).to_csv(args.output, index=False, encoding="utf-8-sig")
            print(json_text({"recommendations": rows[:20], "status": "추천 후보 있음" if rows else "검증 또는 개별 예측 기준 미충족: 추천 보류", "model_gate_reasons": bundle["metadata"]["test"]["gate_reasons"]}))
    except (ValueError, FileNotFoundError) as error:
        parser.exit(2, str(error) + "\n")
    except Exception as error:
        # Network/provider exception messages can contain request URLs; report only type.
        parser.exit(2, "Price model operation failed: " + type(error).__name__ + "\n")


if __name__ == "__main__":
    main()
