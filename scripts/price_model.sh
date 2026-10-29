#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/.."
export LOKY_MAX_CPU_COUNT=2
export PYTHONDONTWRITEBYTECODE=1
PYTHON=python
if [ -x .venv-ml/bin/python ]; then
    PYTHON=.venv-ml/bin/python
fi
COMMAND="${1:-}"
if [ "$COMMAND" = "improve-model" ]; then
    shift
    exec "$PYTHON" -m src.pipeline.model_improvement "$@"
fi
if [ "$COMMAND" = "collect-learning-news" ]; then
    shift
    exec "$PYTHON" -m src.crawler.learning_news_collector "$@"
fi
if [ "$COMMAND" = "news-shadow-model" ]; then
    shift
    exec "$PYTHON" -m src.models.news_shadow_model "$@"
fi
if [ "$COMMAND" = "release-beta" ]; then
    shift
    exec "$PYTHON" -m src.pipeline.ml_beta_release "$@"
fi
if [ "$COMMAND" = "foundation-model" ]; then
    shift
    if [ ! -x .venv-foundation/bin/python ]; then
        echo "Foundation research requires the isolated .venv-foundation runtime." >&2
        exit 2
    fi
    export HF_HUB_DISABLE_TELEMETRY=1
    export HF_HUB_OFFLINE=1
    exec .venv-foundation/bin/python -m src.models.foundation_price_transfer "$@"
fi
if [ "$COMMAND" = "goal-audit" ]; then
    shift
    exec "$PYTHON" -m src.report_generator.reliability_goal_report "$@"
fi
if [ "$COMMAND" = "pairwise-model" ]; then
    shift
    if [ ! -x .venv-ranking/bin/python ]; then
        echo "Pairwise research requires the isolated .venv-ranking runtime." >&2
        exit 2
    fi
    exec .venv-ranking/bin/python -m src.models.pairwise_price_model "$@"
fi
if [ "$COMMAND" = "selective-model" ]; then
    shift
    exec "$PYTHON" -m src.models.selective_price_model "$@"
fi
if [ "$COMMAND" = "swarm-model" ]; then
    shift
    if [ ! -x .venv-neuro/bin/python ]; then
        echo "Peer circuit research requires the isolated .venv-neuro runtime." >&2
        exit 2
    fi
    exec .venv-neuro/bin/python -m src.models.swarm_circuit_experiment "$@"
fi
if [ "$COMMAND" = "neural-model" ]; then
    shift
    if [ ! -x .venv-neuro/bin/python ]; then
        echo "Neural circuit research requires the isolated .venv-neuro runtime." >&2
        exit 2
    fi
    exec .venv-neuro/bin/python -m src.models.neural_circuit_price_model "$@"
fi
if [ "$COMMAND" = "learn-next-open" ]; then
    shift
    exec "$PYTHON" -m src.pipeline.next_open_learning_cycle "$@"
fi
if [ "$COMMAND" = "next-open-model" ]; then
    shift
    exec "$PYTHON" -m src.models.next_open_price_model "$@"
fi
if [ "$COMMAND" = "memory-model" ]; then
    shift
    exec "$PYTHON" -m src.models.adaptive_memory "$@"
fi
if [ "$COMMAND" = "discover-model" ]; then
    shift
    if [ ! -x .venv-discovery/bin/python ]; then
        echo "Formula discovery requires the isolated .venv-discovery runtime." >&2
        exit 2
    fi
    exec .venv-discovery/bin/python -m src.models.formula_discovery "$@"
fi
if [ "$COMMAND" = "distribution-model" ]; then
    shift
    exec "$PYTHON" -m src.models.distributional_selector "$@"
fi
if [ "$COMMAND" = "select-context-model" ]; then
    shift
    exec "$PYTHON" -m src.models.context_model_selection "$@"
fi
if [ "$COMMAND" = "predict-context" ]; then
    shift
    exec "$PYTHON" -m src.models.selected_price_model predict --model-dir data/models/price_forecaster_context_selected "$@"
fi
if [ "$COMMAND" = "freeze-selected" ]; then
    shift
    exec "$PYTHON" -m src.evaluator.selected_model_forward "$@"
fi
if [ "$COMMAND" = "select-model" ]; then
    shift
    exec "$PYTHON" -m src.models.selected_price_model train "$@"
fi
if [ "$COMMAND" = "predict-selected" ]; then
    shift
    exec "$PYTHON" -m src.models.selected_price_model predict "$@"
fi
if [ "$COMMAND" = "predict-research" ]; then
    shift
    exec "$PYTHON" -m src.models.ohlcv_research_predictor "$@"
fi
if [ "$COMMAND" = "update-data" ]; then
    shift
    exec "$PYTHON" -m src.crawler.update_completed_history "$@"
fi
if [ "$COMMAND" = "cycle" ]; then
    shift
    exec "$PYTHON" -m src.pipeline.price_learning_cycle "$@"
fi
if [ "$COMMAND" = "publish" ] || [ "$COMMAND" = "dashboard" ]; then
    shift
    if [ "$COMMAND" = "dashboard" ] && [ "$#" = "0" ] && [ -f docs/price_model.json ]; then
        exec "$PYTHON" -m src.report_generator.dashboard_generator
    fi
    "$PYTHON" -m src.report_generator.supervised_forecast_report "$@" || exit $?
    if [ "$COMMAND" = "dashboard" ]; then
        exec "$PYTHON" -m src.report_generator.dashboard_generator
    fi
    exit 0
fi

DEFAULT_MODEL=""
DATA_ROOT=""
PREVIOUS=""
HAS_MODEL=0
for ARG in "$@"; do
    if [ "$PREVIOUS" = "--data-root" ]; then DATA_ROOT="$ARG"; fi
    case "$ARG" in
        --data-root=*) DATA_ROOT="${ARG#--data-root=}" ;;
        --model-dir|--model-dir=*) HAS_MODEL=1 ;;
    esac
    PREVIOUS="$ARG"
done
if [ "$COMMAND" = "train" ]; then
    if [ -z "$DATA_ROOT" ] || [ ! -f "$DATA_ROOT/history_manifest.json" ]; then
        echo "Training requires --data-root pointing to verified completed OHLCV history." >&2
        exit 2
    fi
    if [ "$HAS_MODEL" = "0" ]; then DEFAULT_MODEL=data/models/price_forecaster_challengers; fi
elif [ "$COMMAND" = "predict" ] || [ "$COMMAND" = "recommend" ]; then
    if [ "$HAS_MODEL" = "0" ]; then DEFAULT_MODEL=data/models/price_forecaster_expanded; fi
fi
if [ -n "$DEFAULT_MODEL" ]; then
    exec "$PYTHON" -m src.models.price_forecaster "$@" --model-dir "$DEFAULT_MODEL"
fi
exec "$PYTHON" -m src.models.price_forecaster "$@"
