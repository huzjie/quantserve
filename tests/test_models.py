from quantserve.models import ModelProfile, QuantResult


def test_model_profile_dict():
    m = ModelProfile(id="x/y", name="Y", family="x", total_params_b=1.0,
                     active_params_b=1.0, architecture="dense", bf16_size_gb=2.0)
    d = m.to_dict()
    assert d["id"] == "x/y"
