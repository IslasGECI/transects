def filter_resident_birds(observed_list_df):
    return observed_list_df[observed_list_df.residentes]["Especie"]
