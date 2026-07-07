"""
Evaluate prior price-based candidates using next trading day returns.
"""

from datetime import datetime
from pathlib import Path

import pandas as pd


RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
PREDICTIONS_DIR = Path("data/predictions")
REPORT_DIR = Path("reports/daily_review")


def normalize_stock_code(value) -> str:
    if value is None or pd.isna(value):
        return ""

    try:
        return str(int(float(value))).zfill(6)
    except Exception:
        return str(value).strip().zfill(6)


def safe_float(value, default=None):
    try:
        if pd.isna(value):
            return default
        return float(value)
    except Exception:
        return default


def latest_price_file(stock_code: str):
    files = sorted(RAW_DIR.glob(f"price_{stock_code}_*.csv"), reverse=True)
    if not files:
        return None
    return files[0]


def read_candidates() -> pd.DataFrame:
    frames = []

    for path in sorted(PROCESSED_DIR.glob("price_based_candidates_*.csv")):
        try:
            df = pd.read_csv(path)
            df["candidate_source_file"] = str(path)
            frames.append(df)
        except Exception:
            continue

    if not frames:
        return pd.DataFrame()

    df = pd.concat(frames, ignore_index=True)
    if "stock_code" in df.columns:
        df["stock_code"] = df["stock_code"].apply(normalize_stock_code)
    return df


def normalize_price_df(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["close"] = pd.to_numeric(df["close"], errors="coerce")
    df["open"] = pd.to_numeric(df.get("open", pd.NA), errors="coerce")
    return df.dropna(subset=["date", "close"]).sort_values("date")


def evaluate_row(row) -> dict:
    stock_code = normalize_stock_code(row.get("stock_code", ""))
    candidate_date = pd.to_datetime(row.get("candidate_date"), errors="coerce")
    action = str(row.get("candidate_action", ""))
    direction = str(row.get("prediction_direction", ""))

    result = row.to_dict()
    result.update(
        {
            "evaluated_at": datetime.today().strftime("%Y-%m-%d"),
            "next_trade_date": pd.NA,
            "next_open_return": pd.NA,
            "next_close_return": pd.NA,
            "price_candidate_result": "pending",
            "evaluation_note": "",
        }
    )

    if not stock_code or pd.isna(candidate_date):
        result["price_candidate_result"] = "invalid_candidate"
        return result

    price_path = latest_price_file(stock_code)
    if price_path is None:
        result["evaluation_note"] = "No price file found."
        return result

    try:
        price_df = normalize_price_df(price_path)
    except Exception as error:
        result["price_candidate_result"] = "price_file_error"
        result["evaluation_note"] = str(error)
        return result

    previous_rows = price_df[price_df["date"] <= candidate_date]
    future_rows = price_df[price_df["date"] > candidate_date]

    if previous_rows.empty or future_rows.empty:
        result["evaluation_note"] = "No next trading day price data available yet."
        return result

    base_close = safe_float(previous_rows.iloc[-1]["close"])
    next_row = future_rows.iloc[0]
    next_open = safe_float(next_row.get("open"))
    next_close = safe_float(next_row.get("close"))

    if not base_close or next_close is None:
        result["price_candidate_result"] = "price_data_missing"
        return result

    next_open_return = (next_open - base_close) / base_close if next_open is not None else pd.NA
    next_close_return = (next_close - base_close) / base_close

    result["next_trade_date"] = next_row["date"].strftime("%Y-%m-%d")
    result["next_open_return"] = round(next_open_return, 4) if not pd.isna(next_open_return) else pd.NA
    result["next_close_return"] = round(next_close_return, 4)

    if direction in {"positive", "neutral_positive"} or action in {"BUY_CANDIDATE", "WATCHLIST"}:
        result["price_candidate_result"] = "success" if next_close_return > 0 else "failure"
    elif direction == "negative" or action == "AVOID":
        result["price_candidate_result"] = "success" if next_close_return < 0 else "failure"
    else:
        result["price_candidate_result"] = "neutral_observed"

    return result


def save_report(df: pd.DataFrame, output_csv: Path) -> str:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    today_display = datetime.today().strftime("%Y-%m-%d")
    output_path = REPORT_DIR / f"{today_display}_price_candidate_evaluation_report.md"

    evaluated = df[df["price_candidate_result"].isin(["success", "failure"])]
    success_count = int((evaluated["price_candidate_result"] == "success").sum()) if not evaluated.empty else 0
    failure_count = int((evaluated["price_candidate_result"] == "failure").sum()) if not evaluated.empty else 0
    success_rate = success_count / len(evaluated) if len(evaluated) else 0

    lines = [
        f"# {today_display} Price Candidate Evaluation",
        "",
        f"Source CSV: `{output_csv}`",
        "",
        f"- Evaluated cases: {len(evaluated)}",
        f"- Success: {success_count}",
        f"- Failure: {failure_count}",
        f"- Success rate: {success_rate * 100:.2f}%",
        "",
        "| Stock | Candidate Date | Action | Result | Next Close Return |",
        "|---|---|---|---|---:|",
    ]

    for _, row in df.head(50).iterrows():
        next_return = safe_float(row.get("next_close_return"), 0)
        lines.append(
            f"| {row.get('stock_code', '')} | {row.get('candidate_date', '')} | "
            f"{row.get('candidate_action', '')} | {row.get('price_candidate_result', '')} | "
            f"{next_return * 100:.2f}% |"
        )

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return str(output_path)


def main():
    print("Evaluating price-based candidates...")

    candidates = read_candidates()
    if candidates.empty:
        print("No price-based candidates found. Evaluation skipped.")
        return

    rows = []
    for _, row in candidates.iterrows():
        try:
            rows.append(evaluate_row(row))
        except Exception as error:
            stock_code = normalize_stock_code(row.get("stock_code", ""))
            print(f"Price candidate evaluation skipped for {stock_code}: {error}")
            continue

    if not rows:
        print("No price candidate evaluations generated.")
        return

    PREDICTIONS_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.today().strftime("%Y%m%d")
    output_csv = PREDICTIONS_DIR / f"price_candidate_evaluation_{today}.csv"
    result_df = pd.DataFrame(rows)
    result_df.to_csv(output_csv, index=False, encoding="utf-8-sig")
    report_path = save_report(result_df, output_csv)

    print(f"Saved {len(result_df)} price candidate evaluations: {output_csv}")
    print(f"Saved report: {report_path}")


if __name__ == "__main__":
    main()
