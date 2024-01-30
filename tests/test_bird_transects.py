import pandas as pd
from pytest import approx

from transects import (
    count_by_specie_and_method,
    count_total_individuals_by_species,
    get_density_by_specie,
    get_total_area,
    get_transect_area,
    join_bird_counts_and_transect_areas,
)


transect_path = "tests/data/bird_transects.csv"
bird_records_path = "tests/data/bird_records.csv"


def test_get_density_by_specie():
    bird_records_df = pd.read_csv(bird_records_path)
    transect_df = pd.read_csv(transect_path)
    obtained = get_density_by_specie(bird_records_df, transect_df)
    expected_columns = 2
    assert len(obtained.columns) == expected_columns
    assert (
        approx(obtained.loc["Setophaga pitiayumii insularis", "densidad"], abs=1e-4) == 53 / 23.6474
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

    transect_from_csv = pd.read_csv(transect_path)
    obtained = get_transect_area(transect_from_csv)
    expected_len = 3
    assert len(obtained) == expected_len
    expected_area_MMAA = 1470 * 60
    assert obtained["MMAA"] == expected_area_MMAA
    expected_area_MMAD = 2000 * 60
    assert obtained["MMAD"] == expected_area_MMAD
    expected_area_MMAB = 2827.4333 * 10
    assert approx(obtained["MMAB"]) == expected_area_MMAB


def test_get_total_area():
    expected = 23.647433388
    transects_info_df = pd.read_csv(transect_path)
    obtained = get_total_area(transects_info_df)
    assert approx(obtained) == expected


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

    records_df = pd.read_csv(bird_records_path)
    obtained = count_by_specie_and_method(records_df)
    expected_actitis_number = 4
    assert obtained.loc[("MMAA", "Actitis macularius")] == expected_actitis_number


def test_count_species_by_method():
    records_dict = {
        "clave_muestreo": ["MMAA", "MMAB", "MMAB", "MMAA", "MMAA", "MMAH"],
        "punto_transecto": ["T1", "1", "2", "T1", "T1", "T3"],
        "Especie": [
            "species 2",
            "species 1",
            "species 1",
            "species 1",
            "species 1",
            "species 2",
        ],
        "n_individuos": [1, 1, 1, 2, 1, 10],
    }
    records_df = pd.DataFrame(records_dict)
    obtained = count_total_individuals_by_species(records_df)
    expected_species_1 = 5
    assert obtained.loc["species 1"] == expected_species_1
    expected_species_2 = 1
    assert obtained.loc["species 2"] == expected_species_2

    records_df = pd.read_csv(bird_records_path)
    obtained = count_total_individuals_by_species(records_df)
    expected_actitis_number = 13
    assert obtained.loc["Actitis macularius"] == expected_actitis_number


def tests_join_bird_counts_and_transect_areas():
    records_dict = {
        "clave_muestreo": ["MMAA", "MMAB", "MMAB", "MMAD"],
        "Especie": [
            "species 2",
            "species 1",
            "species 2",
            "species 1",
        ],
        "n_individuos": [1, 1, 1, 2],
    }
    bird_counts_by_transect_and_species = pd.DataFrame(records_dict)
    transect_areas = {"MMAA": 0.5, "MMAB": 1, "MMAD": 2}
    obtained = join_bird_counts_and_transect_areas(
        bird_counts_by_transect_and_species, transect_areas
    )
    expected_column_names = ["clave_muestreo", "Especie", "n_individuos", "area"]
    assert (obtained.columns.values == expected_column_names).all()
    expected_areas = [0.5, 1, 1, 2]
    obtained_areas = obtained.area.values
    assert obtained_areas == expected_areas
