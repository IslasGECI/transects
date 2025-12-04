from transects.rodent_transects import calculate_trapping_success
from transects.bird_transects import (
    get_mean_density_by_species,
    get_mean_density_by_species_and_transects,
)
from transects.filter_resident_birds import (
    filter_resident_birds,
    filter_species_from_series,
    filter_terrestrial_birds,
)

import pandas as pd
import typer
from typing_extensions import Annotated

cli = typer.Typer()


@cli.command()
def write_bird_records_by_group(
    observed_birds: Annotated[str, typer.Option()],
    bird_records: Annotated[str, typer.Option()],
    group: Annotated[str, typer.Option()],
    output_path: Annotated[str, typer.Option()],
):
    """Filter bird records by a pre-defined group and write to CSV.

    Reads the observed birds CSV and the bird records CSV, filters the
    observed species using a group-specific filter (currently
    "terrestrial" or "resident"), then selects matching records from the
    bird records and writes the result to `output_path`.

    Parameters
    ----------
    observed_birds: str
        Path to a CSV file that lists observed bird species (used for
        selecting which species to keep).
    bird_records: str
        Path to a CSV file containing bird records (observations) that
        will be filtered down to the chosen species.
    group: str
        Filter group to apply. Expected values: "terrestrial" or
        "resident".
    output_path: str
        Path where the filtered records CSV will be written.

    Returns
    -------
    None
        The function writes output to `output_path` and does not return
        a value.
    """

    observed_birds_df = pd.read_csv(observed_birds)
    bird_records_df = pd.read_csv(bird_records)
    filter_dictionary = {"terrestrial": filter_terrestrial_birds, "resident": filter_resident_birds}
    selected_birds_df = filter_dictionary[group](observed_birds_df)
    filter_species_from_series(selected_birds_df, bird_records_df).to_csv(output_path)


@cli.command()
def write_resident_bird_records(
    observed_birds: Annotated[str, typer.Option()],
    bird_records: Annotated[str, typer.Option()],
    output_path: Annotated[str, typer.Option()],
):
    """Write bird records only for resident species to a CSV file.

    Loads `observed_birds` and `bird_records`, selects resident species
    from the observed birds, filters the records for those species, and
    writes the filtered records to `output_path`.

    Parameters
    ----------
    observed_birds: str
        Path to CSV file of observed bird species.
    bird_records: str
        Path to CSV file of bird records (observations).
    output_path: str
        Destination CSV path for resident-only records.

    Returns
    -------
    None
    """

    observed_birds_df = pd.read_csv(observed_birds)
    bird_records_df = pd.read_csv(bird_records)
    resident_birds_df = filter_resident_birds(observed_birds_df)
    filter_species_from_series(resident_birds_df, bird_records_df).to_csv(output_path)


@cli.command()
def write_bird_transect_densities(
    bird_transects: Annotated[str, typer.Option()],
    bird_records: Annotated[str, typer.Option()],
    output_path: Annotated[str, typer.Option()],
):
    """Compute mean bird density by species and transect and write CSV.

    Reads the bird records and transects CSVs, computes mean density per
    species for each transect using `get_mean_density_by_species_and_transects`,
    and writes the resulting table to `output_path`.

    Parameters
    ----------
    bird_transects: str
        Path to CSV file describing transects (used for area/detection
        calculations).
    bird_records: str
        Path to CSV file with bird observation records.
    output_path: str
        Destination CSV path for transect-by-species density results.

    Returns
    -------
    None
    """

    bird_records_df = pd.read_csv(bird_records)
    transects_df = pd.read_csv(bird_transects)
    get_mean_density_by_species_and_transects(bird_records_df, transects_df).to_csv(output_path)


@cli.command()
def write_bird_densities(
    bird_transects: Annotated[str, typer.Option()],
    bird_records: Annotated[str, typer.Option()],
    output_path: Annotated[str, typer.Option()],
):
    """Compute mean bird density by species (across transects) and write CSV.

    Loads transects and bird records, computes mean density per species
    using `get_mean_density_by_species`, and writes the output to
    `output_path`.

    Parameters
    ----------
    bird_transects: str
        Path to CSV file describing transects.
    bird_records: str
        Path to CSV file with bird observation records.
    output_path: str
        Destination CSV path for species-level density results.

    Returns
    -------
    None
    """

    bird_records_df = pd.read_csv(bird_records)
    transects_df = pd.read_csv(bird_transects)
    get_mean_density_by_species(bird_records_df, transects_df).to_csv(output_path)


@cli.command()
def write_rodent_trapping_success(
    rodent_trap_status: Annotated[str, typer.Option()],
    output_path: Annotated[str, typer.Option()],
):
    """Compute rodent trapping success from trap-status CSV and write CSV.

    Reads a CSV describing rodent trap status over trapping sessions,
    calculates trapping success statistics with
    `calculate_trapping_success`, and writes the resulting summary table
    to `output_path`.

    Parameters
    ----------
    rodent_trap_status: str
        Path to CSV file with raw trap status records.
    output_path: str
        Destination path where the trapping success summary CSV will be written.

    Returns
    -------
    None
    """

    trap_status = pd.read_csv(rodent_trap_status)
    calculate_trapping_success(trap_status).to_csv(output_path)
