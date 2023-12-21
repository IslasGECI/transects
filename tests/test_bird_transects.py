import pandas as pd
from pytest import approx

from transects import get_transect_area


def test_get_transect_area():
    transect_dict = {
        "clave_muestreo": ["MMAA", "MMAB", "MMAB", "MMAC", "MMAD"],
        "longitud_transecto": [100, 200, 200, 400, 300],
        "punto_transecto": ["T1", "1", "2", "NA", "T2"],
    }
    transect_df = pd.DataFrame(transect_dict)
    obtained = get_transect_area(transect_df)
    expected_len = 3
    assert len(obtained) == expected_len
    expected_area_MMAA = 6000
    assert obtained["MMAA"] == expected_area_MMAA
    expected_area_MMAD = 18000
    assert obtained["MMAD"] == expected_area_MMAD
    expected_area_MMAB = 5654.866
    assert approx(obtained["MMAB"]) == expected_area_MMAB
