from transects import calculate_rabbit_population_percentils

import pandas as pd


def test_write_rabbit_population_estimate():
    transects_data = pd.read_csv("tests/data/transectos_conejos_isla_clarion.csv")
    obtained_percentiles =calculate_rabbit_population_percentils(transects_data)
    expected_percentiles = {
        "min": 1128.6071615937835,
        "max": 3180.1537328618992,
        "medium": 1128.6071615937835
        }
    assert obtained_percentiles[0] == expected_percentiles["min"]
    assert obtained_percentiles[1] == expected_percentiles["medium"]
    assert obtained_percentiles[2] == expected_percentiles["max"]
