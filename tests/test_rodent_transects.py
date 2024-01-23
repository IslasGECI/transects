from transects import count_rodent_captures_by_site

import pandas as pd


def test_count_rodent_captures_by_site():
    traps_status_data = pd.read_csv("tests/data/rodent_captures.csv")
    obtained = count_rodent_captures_by_site(traps_status_data)
    expected_columns = ["Sitio", "clave_muestreo", "captures"]
    assert (obtained.columns in expected_columns).all()
