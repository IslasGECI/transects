from transects import filter_resident_birds

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
    assert obtained == expected_residents
