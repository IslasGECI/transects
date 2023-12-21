def get_transect_area(transects_info):
    areas = {
        "MMAA": 0,
        "MMAB": "",
        "MMAD": "",
    }
    transect_key = "MMAA"
    areas[transect_key] = calculate_transect_area(transects_info, transect_key)
    areas["MMAD"] = (
        transects_info[transects_info.clave_muestreo == "MMAD"].longitud_transecto.values * 60
    )
    return areas


def calculate_transect_area(transects_info, transect_key):
    return (
        transects_info[transects_info.clave_muestreo == transect_key].longitud_transecto.values * 60
    )
