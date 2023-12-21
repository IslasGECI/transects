def get_transect_area(transects_info):
    areas = {
        "MMAA": 0,
        "MMAB": "",
        "MMAD": "",
    }
    transect_key = ["MMAA", "MMAD"]
    for key in transect_key:
        areas[key] = calculate_transect_area(transects_info, key)
    return areas


def calculate_transect_area(transects_info, transect_key):
    area_differential = 60
    return (
        transects_info[transects_info.clave_muestreo == transect_key].longitud_transecto.values
        * area_differential
    )
