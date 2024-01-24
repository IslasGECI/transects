from transects import get_density_by_specie
import typer

cli = typer.Typer()


@cli.command()
def write_bird_densities(bird_transects: str = "", bird_records: str = "", output_path: str = ""):
    get_density_by_specie(bird_records, bird_transects).to_csv(output_path)
