from transects import get_density_by_specie

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
