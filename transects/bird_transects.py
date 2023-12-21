import numpy as np


def get_transect_area(transects_info):
    areas = {}
    transect_key = ["MMAA", "MMAB", "MMAD"]
    area_differentials = {"MMAA": 60, "MMAB": (np.pi * (30) ** 2), "MMAD": 60}
    for key in transect_key:
        areas[key] = calculate_transect_area(transects_info, key, area_differentials)
    return areas


def calculate_transect_area(transects_info, transect_key, area_differentials):
    transect_length = get_transect_length(transects_info, transect_key)
    if transect_key != "MMAB":
        return transect_length * area_differentials[transect_key]
    else:
        number_points = len(transect_length)
        return number_points * area_differentials[transect_key]


def get_transect_length(transects_info, transect_key):
    transect_mask = transects_info.clave_muestreo == transect_key
    return transects_info[transect_mask].longitud_transecto.values
