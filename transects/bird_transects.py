def get_transect_area(transects_info):
    areas = {
        "MMAA": 0,
        "MMAB": "",
        "MMAD": "",
    }
    areas["MMAA"] = (
        transects_info[transects_info.clave_muestreo == "MMAA"].longitud_transecto.values * 60
    )
    return areas
