from quantserve.cluster import TopologyPlanner, GPU


def test_single_gpu():
    r = TopologyPlanner().plan([GPU(0, "RTX 4090", 24576)])
    assert r["gpus"] == 1


def test_nvlink_hint():
    gpus = [GPU(i, "NVIDIA H100", 81920) for i in range(8)]
    r = TopologyPlanner().plan(gpus)
    assert r["interconnect"] == "nvlink"
