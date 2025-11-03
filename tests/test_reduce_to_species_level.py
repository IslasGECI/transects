from transects.reduce_to_species_level import add_species_level_column, reduce_to_species_level


import pandas as pd


def test_add_species_level_column():
    bird_records_df = pd.DataFrame(
        {
            "Especie": [
                "Amazona oratrix tresmariae",
                "Amazona oratrix",
                "Leptotila verreauxi capitalis",
            ]
        }
    )
    obtained = add_species_level_column(bird_records_df)
    assert "species_level_name" in obtained.columns


def test_reduce_to_species_level():
    subspecies_name = "Amazona oratrix tresmariae"
    obtained = reduce_to_species_level(subspecies_name)
    expected = "Amazona oratrix"
    assert obtained == expected
