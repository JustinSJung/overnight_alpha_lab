"""Small prespecified AutoML search space; never generated or expanded at runtime."""
BASELINE = 'extra_trees_504'
FAMILIES = {
    BASELINE: {'factory': 'extra_trees', 'training_sessions': 504, 'calibration_sessions': 60},
    'auto_linear_504_v1': {'factory': 'linear', 'training_sessions': 504, 'calibration_sessions': 60},
    'auto_hgb_504_v1': {'factory': 'hgb_shallow', 'training_sessions': 504, 'calibration_sessions': 60},
    'auto_extra_252_v1': {'factory': 'extra_trees', 'training_sessions': 252, 'calibration_sessions': 60},
}


def family_spec(name):
    if name not in FAMILIES:
        raise ValueError('Unregistered model family; do not silently expand the search space.')
    return FAMILIES[name].copy()
