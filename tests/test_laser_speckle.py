import pytest
import graphics.laser_speckle as mod

CASES = [
    ("speckle_decorrelate", (1,)),
    ("phase_perturb_continuous", (1,)),
    ("overlap_luminance_adapt", (1,)),
    ("coord_space_separate", (1,)),
    ("thermal_drift_correct", (1,)),
    ("speckle_contrast_metric", (1,)),
    ("load_laser_project", (1,)),
    ("align_projectors", (1,)),
    ("suppress_speckle", (1,)),
    ("present_laser", (1,)),
    ("validate_laser", (1,)),
    ("metrics_laser", (1,)),
    ("audit_laser", (1,)),
    ("fallback_laser", (1,)),
    ("determinism_laser", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
