import pandas as pd
from pytest import approx

from transects import (
    count_by_specie_and_method,
    get_transect_area,
    count_total_individuals_by_species,
)


transect_dict = {
    "clave_muestreo": ["MMAA", "MMAB", "MMAB", "MMAC", "MMAD"],
    "longitud_transecto": [100, 200, 200, 400, 300],
    "punto_transecto": ["T1", "1", "2", "NA", "T2"],
}
transect_df = pd.DataFrame(transect_dict)


def test_get_transect_area():
    obtained = get_transect_area(transect_df)
    expected_len = 3
    assert len(obtained) == expected_len
    expected_area_MMAA = 6000
    assert obtained["MMAA"] == expected_area_MMAA
    expected_area_MMAD = 18000
    assert obtained["MMAD"] == expected_area_MMAD
    expected_area_MMAB = 5654.866
    assert approx(obtained["MMAB"]) == expected_area_MMAB

    transect_from_csv = pd.read_csv("tests/data/bird_transects.csv")
    obtained = get_transect_area(transect_from_csv)
    expected_len = 3
    assert len(obtained) == expected_len
    expected_area_MMAA = 1470 * 60
    assert obtained["MMAA"] == expected_area_MMAA
    expected_area_MMAD = 2000 * 60
    assert obtained["MMAD"] == expected_area_MMAD
    expected_area_MMAB = 2827.4333 * 10
    assert approx(obtained["MMAB"]) == expected_area_MMAB


def tests_count_by_specie_and_method():
    records_dict = {
        "clave_muestreo": ["MMAA", "MMAA"],
        "punto_transecto": ["T1", "T1"],
        "Especie": [
            "species 1",
            "species 1",
        ],
        "n_individuos": [1, 2],
    }
    records_df = pd.DataFrame(records_dict)
    obtained = count_by_specie_and_method(records_df)
    expected_MMAA_species = 3
    assert obtained.loc["MMAA", "species 1"] == expected_MMAA_species

    records_dict = {
        "clave_muestreo": ["MMAD", "MMAD", "MMAA", "MMAB", "MMAB"],
        "punto_transecto": ["T1", "T1", "T3", "2", "3"],
        "Especie": [
            "species 1",
            "species 1",
            "species 2",
            "species 3",
            "species 1",
        ],
        "n_individuos": [1, 2, 8, 4, 5],
    }
    records_df = pd.DataFrame(records_dict)
    obtained = count_by_specie_and_method(records_df)
    expected_MMAA_species = 8
    assert obtained.loc["MMAA", "species 2"] == expected_MMAA_species

    records_df = pd.read_csv("tests/data/bird_records.csv")
    obtained = count_by_specie_and_method(records_df)
    obtained.to_csv("tests/data/bird_count.csv")


def test_count_species_by_method():
    grouped_data = pd.DataFrame(
        {"n_individuos": [1, 2, 3, 10]},
    )
    grouped_data.index = pd.MultiIndex.from_arrays(
        [["MMAA", "MMAB", "MMAA", "MMAH"], ["species 2", "species 1", "species 1", "species 2"]],
        names=["clave_muestreo", "Especie"],
    )
    print(grouped_data.index.get_level_values("Especie").unique())
    obtained = count_total_individuals_by_species(grouped_data)
    print(obtained)
    expected_species_1 = 5
    assert obtained.loc["species 1"].values == expected_species_1
    expected_species_2 = 1
    assert obtained.loc["species 2"].values == expected_species_2
