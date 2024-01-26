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
    print(obtained)
    expected_residents = "Anas discors"
    assert obtained.values[0] == expected_residents
