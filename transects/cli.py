from .rodent_transects import calculate_trapping_success
from .bird_transects import get_density_by_specie, get_density_by_species_and_transects
from .filter_resident_birds import filter_resident_birds, filter_resident_records

import pandas as pd
import typer
from typing_extensions import Annotated

cli = typer.Typer()


@cli.command()
def write_resident_bird_records(
    observed_birds: Annotated[str, typer.Option()],
    bird_records: Annotated[str, typer.Option()],
    output_path: Annotated[str, typer.Option()],
):
    observed_birds_df = pd.read_csv(observed_birds)
    bird_records_df = pd.read_csv(bird_records)
    resident_birds_df = filter_resident_birds(observed_birds_df)
    filter_resident_records(resident_birds_df, bird_records_df).to_csv(output_path)


@cli.command()
def write_bird_transect_densities(
    bird_transects: Annotated[str, typer.Option()],
    bird_records: Annotated[str, typer.Option()],
    output_path: Annotated[str, typer.Option()],
):
    bird_records_df = pd.read_csv(bird_records)
    transects_df = pd.read_csv(bird_transects)
    get_density_by_species_and_transects(bird_records_df, transects_df).to_csv(output_path)


@cli.command()
def write_bird_densities(
    bird_transects: Annotated[str, typer.Option()],
    bird_records: Annotated[str, typer.Option()],
    output_path: Annotated[str, typer.Option()],
):
    bird_records_df = pd.read_csv(bird_records)
    transects_df = pd.read_csv(bird_transects)
    get_density_by_specie(bird_records_df, transects_df).to_csv(output_path)


@cli.command()
def write_rodent_trapping_success(
    rodent_trap_status: Annotated[str, typer.Option()],
    output_path: Annotated[str, typer.Option()],
):
    trap_status = pd.read_csv(rodent_trap_status)
    calculate_trapping_success(trap_status).to_csv(output_path)
