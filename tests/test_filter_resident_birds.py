from transects import filter_resident_birds, filter_resident_records

import pandas as pd


def test_filter_resident_birds():
    observed_list_df = pd.DataFrame(
        {
            "Especie": ["Calidris alba", "Anas discors", "Columbina passerina"],
            "residentes": [False, True, False],
        }
    )
    obtained = filter_resident_birds(observed_list_df)
    expected_residents = "Anas discors"
    assert obtained.values[0] == expected_residents


def test_filter_resident_records():
    records_list_df = pd.DataFrame(
        {
            "Especie": [
                "Calidris alba",
                "Calidris alba",
                "Anas discors",
                "Columbina passerina",
                "Anas discors",
            ],
            "n_individuos": [5, 3, 8, 2, 2],
        }
    )
    resident_birds_df = pd.Series({"Especie": ["Columbina passerina"]})
    obtained = filter_resident_records(resident_birds_df, records_list_df)
    expected_rows = 1
    assert len(obtained) == expected_rows
    resident_birds_df = pd.Series({"Especie": ["Anas discors"]})
    obtained = filter_resident_records(resident_birds_df, records_list_df)
    expected_rows = 2
    assert len(obtained) == expected_rows
