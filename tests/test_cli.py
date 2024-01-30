from transects import cli


from typer.testing import CliRunner
import os


transect_path = "tests/data/bird_transects.csv"
bird_records_path = "tests/data/bird_records.csv"

runner = CliRunner()


def test_write_bird_transect_densities():
    result = runner.invoke(cli, ["write-bird-transect-densities", "--help"])
    assert result.exit_code == 0

    output_path = "tests/bird_transect_densities.csv"

    if os.path.exists(output_path):
        os.remove(output_path)

    result = runner.invoke(
        cli,
        [
            "write-bird-transect-densities",
            "--bird-transects",
            transect_path,
            "--bird-records",
            bird_records_path,
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    assert os.path.exists(output_path)
    # os.remove(output_path)


def test_write_bird_densities():
    result = runner.invoke(cli, ["write-bird-densities", "--help"])
    assert result.exit_code == 0

    output_path = "tests/bird_densities.csv"

    if os.path.exists(output_path):
        os.remove(output_path)

    result = runner.invoke(
        cli,
        [
            "write-bird-densities",
            "--bird-transects",
            transect_path,
            "--bird-records",
            bird_records_path,
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    assert os.path.exists(output_path)
    os.remove(output_path)


def test_write_rodent_trapping_success():
    result = runner.invoke(cli, ["write-rodent-trapping-success", "--help"])
    assert result.exit_code == 0

    output_path = "tests/rodent_trapping_success.csv"

    if os.path.exists(output_path):
        os.remove(output_path)

    traps_status_data_path = "tests/data/rodent_captures.csv"
    result = runner.invoke(
        cli,
        [
            "write-rodent-trapping-success",
            "--rodent-trap-status",
            traps_status_data_path,
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    assert os.path.exists(output_path)
    os.remove(output_path)


def test_write_resident_bird_records():
    result = runner.invoke(cli, ["write-resident-bird-records", "--help"])
    assert result.exit_code == 0

    output_path = "tests/resident_records.csv"
    observed_path = "tests/data/observed_bird_species.csv"

    if os.path.exists(output_path):
        os.remove(output_path)

    result = runner.invoke(
        cli,
        [
            "write-resident-bird-records",
            "--observed-birds",
            observed_path,
            "--bird-records",
            bird_records_path,
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    assert os.path.exists(output_path)
