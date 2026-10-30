"""Purged, matched historical development replay. Never a promotion certificate."""
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from threadpoolctl import threadpool_limits

from src.features.next_open_dataset import COLUMNS, build_next_open_dataset
from src.models.monthly_price_walkforward import monthly_split
from src.models.next_open_price_model import load_inputs
from src.models.price_forecaster import date_weights, fit_estimator
from src.models.relative_price_selection import rank_candidates
from src.models.selected_price_model import factories, partition_info, to_logits
from src.research.programs import transform


def development_folds(cohort, policy):
    known = cohort[cohort.target.notna()]
    dates = sorted(cohort.loc[cohort.expected_target_date.notna(), 'signal_date'].unique())
    needed = policy['folds'] * policy['screen_sessions']
    if len(dates) < needed + policy['training_sessions'] + policy['calibration_sessions'] + 10:
        raise ValueError('Insufficient history for fixed purged research folds.')
    chosen = dates[-needed:]
    folds = []
    for i in range(policy['folds']):
        validation_days = chosen[i * policy['screen_sessions']:(i + 1) * policy['screen_sessions']]
        start = pd.Timestamp(validation_days[0])
        fit_asof = max(day for day in dates if day < start)
        train, calibration = monthly_split(known, as_of=fit_asof,
                                           training_sessions=policy['training_sessions'],
                                           calibration_sessions=policy['calibration_sessions'])
        validation = cohort[cohort.signal_date.isin(validation_days)].copy().reset_index(drop=True)
        if calibration.label_available_date.max() >= start or train.label_available_date.max() >= calibration.signal_date.min():
            raise ValueError('Research fitting labels cross into a later partition.')
        folds.append((train, calibration, validation))
    return folds


def probability(train, calibration, validation, program=None):
    features = lambda part: transform(program, part) if program else part[COLUMNS].to_numpy(dtype=float)
    learner = program['learner'] if program else 'hgb_shallow'
    with threadpool_limits(limits=2):
        model = fit_estimator(factories()[learner], features(train), train.target.astype(int), date_weights(train))
        fit_calibration = model.predict_proba(features(calibration))[:, 1]
        calibrator = LogisticRegression(C=1., solver='liblinear', max_iter=1000, random_state=42)
        calibrator.fit(to_logits(fit_calibration), calibration.target.astype(int), sample_weight=date_weights(calibration))
        result = calibrator.predict_proba(to_logits(model.predict_proba(features(validation))[:, 1]))[:, 1]
    if not np.isfinite(result).all() or np.any((result < 0) | (result > 1)):
        raise ValueError('Invalid research probabilities.')
    return result


def metrics(frame, values):
    scored = frame.copy().reset_index(drop=True)
    scored['research_probability'] = values
    observed = scored[scored.target.notna()]
    if observed.empty:
        raise ValueError('No mature research outcomes.')
    daily_brier = ((observed.research_probability - observed.target) ** 2).groupby(observed.signal_date).mean()
    selected = rank_candidates(scored[scored.research_probability.ge(.6)], 'research_probability', 5)
    resolved = selected[selected.target.notna()]
    return dict(input_candidates=len(scored), evaluated_cases=len(observed),
                unresolved_cases=int(scored.target.isna().sum()),
                signal_dates=int(scored.signal_date.nunique()), date_brier=float(daily_brier.mean()),
                selected_cases=len(selected), selected_evaluated_cases=len(resolved),
                selected_signal_dates=int(selected.signal_date.nunique()),
                selected_missing_outcomes=int(selected.target.isna().sum()),
                selected_success_rate=float(resolved.target.mean()) if len(resolved) else None,
                conditional_mean_net_return_proxy=float(resolved.net_return_proxy.mean()) if len(resolved) else None)


def evaluate_program(data_root, as_of, program, policy):
    inputs, _ = load_inputs(data_root, as_of)
    cohort, _ = build_next_open_dataset(inputs, as_of)
    records, candidate_parts, control_parts, constants = [], [], [], []
    for number, (train, calibration, validation) in enumerate(development_folds(cohort, policy), 1):
        candidate = probability(train, calibration, validation, program)
        control = probability(train, calibration, validation)
        prior = float(np.average(calibration.target, weights=date_weights(calibration)))
        candidate_metrics, control_metrics = metrics(validation, candidate), metrics(validation, control)
        records.append(dict(fold=number, train=partition_info(train), calibration=partition_info(calibration),
                            development=partition_info(validation), candidate=candidate_metrics, control=control_metrics))
        candidate_parts.append(validation.assign(research_probability=candidate))
        control_parts.append(validation.assign(research_probability=control))
        constants.append(validation.assign(research_probability=prior))
    candidate = pd.concat(candidate_parts, ignore_index=True)
    control = pd.concat(control_parts, ignore_index=True)
    constant = pd.concat(constants, ignore_index=True)
    if candidate.duplicated(['stock_code', 'signal_date']).any():
        raise ValueError('Development folds repeat stock/date cases.')
    score = metrics(candidate, candidate.research_probability.to_numpy())
    reference = metrics(control, control.research_probability.to_numpy())
    past_constant = metrics(constant, constant.research_probability.to_numpy())
    score.update(control_date_brier=reference['date_brier'], past_constant_date_brier=past_constant['date_brier'],
                 development_brier_improvement=reference['date_brier'] - score['date_brier'],
                 folds_improved=sum(row['candidate']['date_brier'] < row['control']['date_brier'] for row in records))
    reasons = []
    if score['development_brier_improvement'] <= 0: reasons.append('no_error_reduction_against_matched_control')
    if score['date_brier'] >= past_constant['date_brier']: reasons.append('does_not_beat_past_constant')
    if score['folds_improved'] < policy['folds']: reasons.append('unstable_across_development_periods')
    if score['unresolved_cases']: reasons.append('development_outcomes_incomplete')
    if score['selected_evaluated_cases'] < 100: reasons.append('too_few_selected_development_cases')
    score['research_screen_passed'] = not reasons
    score['screen_reasons'] = reasons
    return dict(metrics=score, folds=records, evidence='reused_historical_development_only',
                future_validation_required=True, production_promotion=False, recommendation_enabled=False)
