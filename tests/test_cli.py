from transects import cli


from typer.testing import CliRunner
import os


transect_path = "tests/data/bird_transects.csv"
bird_records_path = "tests/data/bird_records.csv"

runner = CliRunner()


def test_write_bird_densities():
    result = runner.invoke(cli, ["write-bird-densities", "--help"])
    assert result.exit_code == 0

    output_path = "tests/bird_densities.csv"
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

    assert os.path.exists(output_path)
