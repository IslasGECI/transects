import numpy as np
import pandas as pd


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


def count_total_individuals_by_species(grouped_data):
    claves = ["MMAA", "MMAB", "MMAD"]
    grouped_data.query(f"clave_muestreo.isin({claves})", inplace=True)
    df = pd.DataFrame({"n_individuos": []})
    df_indexes = grouped_data.index.get_level_values("Especie").unique()
    for species in df_indexes:
        df.loc[species] = grouped_data.xs(species, level="Especie").sum().values
    return df
