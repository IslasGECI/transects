import pandas as pd
from pytest import approx

from transects import count_by_specie_and_method, get_transect_area


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
    expected = {"MMAA": {"species 1": 3}}
    assert obtained == expected

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
    expected = {"MMAA": {"species 2": 8}}
    assert obtained == expected
