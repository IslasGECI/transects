import numpy as np
import pandas as pd


def get_density_by_specie(bird_records_df, transects_info_df):
    counts = count_total_individuals_by_species(bird_records_df).to_frame()
    total_area = get_total_area(transects_info_df)
    counts["densidad"] = counts.n_individuos / total_area
    return counts


def get_total_area(transects_info_df):
    areas = get_transect_area(transects_info_df)
    total = 0.0
    for value in areas.values():
        total += value
    return total / 10_000


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


def join_bird_counts_and_transect_areas(bird_counts_by_transect_and_species, transect_areas):
    transect_areas_df = pd.DataFrame.from_dict(transect_areas, orient="index", columns=["area"])
    joined = bird_counts_by_transect_and_species.join(transect_areas_df, on="clave_muestreo")
    return joined
