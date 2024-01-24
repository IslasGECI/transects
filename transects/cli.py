from .rodent_transects import calculate_trapping_success
from .bird_transects import get_density_by_specie

import pandas as pd
import typer
from typing_extensions import Annotated

cli = typer.Typer()


@cli.command()
def write_bird_densities(
    bird_transects: Annotated[str, typer.Option()],
    bird_records: Annotated[str, typer.Option()],
    output_path: Annotated[str, typer.Option()],
):
    get_density_by_specie(bird_records, bird_transects).to_csv(output_path)


@cli.command()
def write_rodent_trapping_success(
    rodent_trap_status: Annotated[str, typer.Option()],
    output_path: Annotated[str, typer.Option()],
):
    trap_status = pd.read_csv(rodent_trap_status)
    calculate_trapping_success(trap_status).to_csv(output_path)
