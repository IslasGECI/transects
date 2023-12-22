import numpy as np
import pandas as pd


def get_total_area(transects_info_path):
    transects_info = pd.read_csv(transects_info_path)
    areas = get_transect_area(transects_info)
    total = 0.0
    for value in areas.values():
        total += value
    return total


def get_transect_area(transects_info):
    area_differentials = {"MMAA": 60, "MMAB": (np.pi * (30) ** 2), "MMAD": 60}
    areas = {}
    for key in area_differentials.keys():
        areas[key] = calculate_transect_area(transects_info, key, area_differentials)
    return areas


def calculate_transect_area(transects_info, transect_key, area_differentials):
    transect_mask = transects_info.clave_muestreo == transect_key
    transect_length = get_transect_length(transects_info, transect_mask)
    are_transects = transects_info[transect_mask].punto_transecto.str.contains("T").all()
    if are_transects:
        return transect_length * area_differentials[transect_key]
    else:
        number_points = len(transect_length)
        return number_points * area_differentials[transect_key]


def get_transect_length(transects_info, transect_mask):
    return transects_info[transect_mask].longitud_transecto.values


def count_by_specie_and_method(records_df):
    return records_df.groupby(["clave_muestreo", "Especie"])["n_individuos"].agg("sum")


def count_total_individuals_by_species(records_df):
    claves = ["MMAA", "MMAB", "MMAD"]
    records_df.query(f"clave_muestreo.isin({claves})", inplace=True)
    return records_df.groupby(["Especie"])["n_individuos"].agg("sum")
