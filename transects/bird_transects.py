import numpy as np


def get_transect_area(transects_info):
    area_differentials = {"MMAA": 60, "MMAB": (np.pi * (30) ** 2), "MMAD": 60}
    areas = {}
    for key in area_differentials.keys():
        areas[key] = calculate_transect_area(transects_info, key, area_differentials)
    return areas


def calculate_transect_area(transects_info, transect_key, area_differentials):
    transect_length = get_transect_length(transects_info, transect_key)
    number_points = len(transect_length)
    transect_mask = transects_info.clave_muestreo == transect_key
    are_transects = transects_info[transect_mask].punto_transecto.str.contains("T").all()
    if are_transects:
        return transect_length * area_differentials[transect_key]
    else:
        return number_points * area_differentials[transect_key]


def get_transect_length(transects_info, transect_key):
    transect_mask = transects_info.clave_muestreo == transect_key
    return transects_info[transect_mask].longitud_transecto.values
