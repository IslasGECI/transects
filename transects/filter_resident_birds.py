def filter_resident_birds(observed_list_df):
    return observed_list_df[observed_list_df.residentes]["Especie"]


def filter_resident_records(residents_birds_df, records_list_df):
    records_list_indexed = records_list_df.set_index("Especie")
    return records_list_indexed.loc[residents_birds_df]
