import numpy as np


def get_transect_area(transects_info):
    areas = {
        "MMAA": 0,
        "MMAB": "",
        "MMAD": "",
    }
    transect_key = ["MMAA", "MMAB", "MMAD"]
    for key in transect_key:
        areas[key] = calculate_transect_area(transects_info, key)
    return areas


def calculate_transect_area(transects_info, transect_key):
    transect_length = get_transect_length(transects_info, transect_key)
    area_differentials = {"MMAA": 60, "MMAB": (np.pi * (30) ** 2) / transect_length, "MMAD": 60}
    return transect_length.sum() * area_differentials[transect_key]


def get_transect_length(transects_info, transect_key):
    transect_mask = transects_info.clave_muestreo == transect_key
    return transects_info[transect_mask].longitud_transecto.values
