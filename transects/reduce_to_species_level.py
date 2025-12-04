import pandas as pd


def add_species_level_column(bird_records_df: pd.DataFrame) -> pd.DataFrame:
    bird_records_df_copy = bird_records_df.copy()
    bird_records_df_copy["species_level_name"] = bird_records_df_copy["Especie"].apply(
        reduce_to_species_level
    )
    return bird_records_df_copy


def reduce_to_species_level(bird_name: str) -> str:
    return " ".join(bird_name.split(" ")[:2])
