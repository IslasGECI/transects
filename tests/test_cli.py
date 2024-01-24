from transects import cli


from typer.testing import CliRunner


transect_path = "tests/data/bird_transects.csv"
bird_records_path = "tests/data/bird_records.csv"

runner = CliRunner()


def test_write_bird_densities():
    result = runner.invoke(cli, ["write-bird-densities", "--help"])
    assert result.exit_code == 0
