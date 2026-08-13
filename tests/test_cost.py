from quantserve.cost import CostCalculator


def test_local_positive():
    c = CostCalculator()
    assert c.local_monthly() > 0


def test_compare_cloud():
    c = CostCalculator()
    r = c.compare("deepseek/deepseek-v4-pro", 500)
    assert r.cloud_monthly_usd > 0
    assert r.local_monthly_usd > 0
