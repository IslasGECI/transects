from transects import count_rodent_captures_by_site, calculate_rodent_effort_by_site

import pandas as pd

traps_status_data = pd.read_csv("tests/data/rodent_captures.csv")


def test_count_rodent_captures_by_site():
    obtained = count_rodent_captures_by_site(traps_status_data)
    expected_columns = ["Sitio", "captures"]
    assert obtained.columns in expected_columns

    obtained_captures = obtained.loc["Laguna del Toro", "captures"]
    expected_captures = 1
    assert obtained_captures == expected_captures


def test_calculate_rodent_effort_by_site():
    obtained = calculate_rodent_effort_by_site(traps_status_data)
    expected_columns = ["Sitio", "effort"]
    are_columns = [column in expected_columns for column in obtained.columns]
    assert all(are_columns)
    expected_number_of_rows = 4
    obtained_number_of_rows = len(obtained)
    assert obtained_number_of_rows == expected_number_of_rows
    expected_effort_laguna_del_toro = 45
    assert obtained.loc["Laguna del Toro", "effort"] == expected_effort_laguna_del_toro
    expected_effort_laguna_del_toro = 44
    assert obtained.loc["Arroyo al Zacatal", "effort"] == expected_effort_laguna_del_toro
