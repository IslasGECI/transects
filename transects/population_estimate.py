from geci_distance import GECI_Distance
from bootstrapping_tools import boostrapping_feature

import numpy as np

def calculate_rabbit_population_percentils(transects_data):
    population_estimations = []
    transects_data = transects_data[transects_data["Temporada"] == 2021]
    for _, data in transects_data.groupby(by="Transecto"):
        project = GECI_Distance(data.Cantidad_individuos, data.Distancia)
        project.set_line_width(100)
        project.set_line_length(1000)
        project.set_study_area(data.Area_isla.iloc[0])
        population_estimations.append(project.estimate_population())

    estimation_bootstrap = boostrapping_feature(population_estimations)

    minimum_value = np.percentile(estimation_bootstrap, 2.5)
    medium_value = np.percentile(estimation_bootstrap, 50)
    maximum_value = np.percentile(estimation_bootstrap, 97.5)
    return [minimum_value, medium_value, maximum_value]
