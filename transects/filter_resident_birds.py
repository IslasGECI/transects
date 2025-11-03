def filter_resident_birds(observed_list_df):
    return observed_list_df[observed_list_df.residentes]["Especie"]


def filter_terrestrial_birds(observed_list_df):
    return observed_list_df[observed_list_df.Grupo == "Terrestre"]["Especie"]


def filter_species_from_series(selected_birds_df, records_list_df):
    records_list_indexed = records_list_df.set_index("Especie")
    return records_list_indexed.loc[selected_birds_df]
