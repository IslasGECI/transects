from geci_distance import GECI_Distance
from bootstrapping_tools import boostrapping_feature

import numpy as np
import json


def write_estimations(output_path, intervals):
    with open(output_path, "w") as exit_file:
        json.dump(
            {
                "minimo": f"{np.around(intervals[1] - intervals[0]):,.0f}",
                "media": f"{np.around(intervals[1]):,.0f}",
                "maximo": f"{np.around(intervals[2] - intervals[1]):,.0f}",
            },
            exit_file,
        )


def calculate_rabbit_population_percentils(transects_data, season=2021):
    population_estimations = calculate_population_estimate_by_season_and_transect(
        transects_data, season
    )
    estimation_bootstrap = boostrapping_feature(population_estimations)
    return get_confidence_interval(estimation_bootstrap)


def get_confidence_interval(estimation_bootstrap):
    minimum_value = np.percentile(estimation_bootstrap, 2.5)
    medium_value = np.percentile(estimation_bootstrap, 50)
    maximum_value = np.percentile(estimation_bootstrap, 97.5)
    return [minimum_value, medium_value, maximum_value]


def calculate_population_estimate_by_season_and_transect(transects_data, season=2021):
    population_estimations = []
    transects_data = transects_data[transects_data["Temporada"] == season]
    for _, data in transects_data.groupby(by="Transecto"):
        project = GECI_Distance(data.Cantidad_individuos, data.Distancia)
        project.set_line_width(100)
        project.set_line_length(1000)
        project.set_study_area(data.Area_isla.iloc[0])
        population_estimations.append(project.estimate_population())
    return population_estimations
