import numpy as np
import pandas as pd


def get_density_by_species_and_transects(bird_records_df, transect_df):
    bird_counts_by_transect_and_species = count_by_specie_and_method(bird_records_df).to_frame()
    transect_areas = get_transect_area(transect_df)
    joined = join_bird_counts_and_transect_areas(
        bird_counts_by_transect_and_species, transect_areas
    )
    joined["density"] = joined["n_individuos"] / joined["area"]
    return joined


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
    return total


def get_transect_area(transects_info):
    area_differentials = {"MMAA": 60, "MMAB": (np.pi * (30) ** 2), "MMAD": 60}
    areas = {}
    square_meters_to_hectares = 10_000
    for key in area_differentials.keys():
        transect_area = calculate_transect_area(transects_info, key, area_differentials)
        areas[key] = transect_area / square_meters_to_hectares
    return areas


def calculate_transect_area(transects_info, transect_key, area_differentials):
    transect_mask = transects_info.clave_muestreo == transect_key
    transect_length = get_transect_length(transects_info, transect_mask)
    are_transects = transects_info[transect_mask].punto_transecto.str.contains("T").all()
    number_points = len(transect_length)
    if are_transects:
        return transect_length[0] * area_differentials[transect_key]
    return number_points * area_differentials[transect_key]


def get_transect_length(transects_info, transect_mask):
    return transects_info[transect_mask].longitud_transecto.values


def count_by_specie_and_method(records_df):
    filtered_records = filter_transects_of_interes(records_df)
    return filtered_records.groupby(["clave_muestreo", "Especie"])["n_individuos"].agg("sum")


def count_total_individuals_by_species(records_df):
    filtered_records = filter_transects_of_interes(records_df)
    return filtered_records.groupby(["Especie"])["n_individuos"].agg("sum")


def filter_transects_of_interes(records_df):
    claves = ["MMAA", "MMAB", "MMAD"]
    return records_df.query(f"clave_muestreo.isin({claves})")


def join_bird_counts_and_transect_areas(bird_counts_by_transect_and_species, transect_areas):
    transect_areas_df = pd.DataFrame.from_dict(transect_areas, orient="index", columns=["area"])
    joined = bird_counts_by_transect_and_species.join(transect_areas_df, on="clave_muestreo")
    return joined
