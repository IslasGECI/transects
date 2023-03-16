from transects import (
    calculate_rabbit_population_percentils,
    calculate_population_estimate_by_season_and_transect,
    write_estimations,
)

import os
import pandas as pd


transects_data = pd.read_csv("tests/data/transectos_conejos_isla_clarion.csv")
expected_2022_percentiles = {
    "min": 882.1903270242863,
    "medium": 1520.9899638266606,
    "max": 2947.4381238658193,
}


def test_write_rabbit_population_estimate():
    obtained_percentiles = calculate_rabbit_population_percentils(transects_data)
    expected_percentiles = {
        "min": 1128.6071615937835,
        "max": 2974.91369532452,
        "medium": 1128.6071615937835,
    }
    assert obtained_percentiles[0] == expected_percentiles["min"]
    assert obtained_percentiles[1] == expected_percentiles["medium"]
    assert obtained_percentiles[2] == expected_percentiles["max"]

    season = 2022
    obtained_2022_percentiles = calculate_rabbit_population_percentils(transects_data, season)
    assert obtained_2022_percentiles[0] == expected_2022_percentiles["min"]
    assert obtained_2022_percentiles[1] == expected_2022_percentiles["medium"]
    assert obtained_2022_percentiles[2] == expected_2022_percentiles["max"]


def test_calculate_population_estimate_by_season_and_transect():
    season = 2022
    obtained = calculate_population_estimate_by_season_and_transect(transects_data, season)
    obtained_length = len(obtained)
    expected_length = 4
    assert obtained_length == expected_length


def test_write_estimations():
    output_path = "tests/data/rabbit_estimation.json"
    intervals = list(expected_2022_percentiles.values())
    print(intervals)
    write_estimations(output_path, intervals)
    assert os.path.exists(output_path)
