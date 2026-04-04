from cocijo.cli import app
from typer.testing import CliRunner
import os

runner = CliRunner()


def test_write_daily_rain():
    result = runner.invoke(app, ["write-daily-rain-plot", "--help"])
    assert result.exit_code == 0
    data_path = "tests/data/registro_lluvias_for_test.csv"
    output_path = "tests/data/lluvia_diaria.png"

    if os.path.isfile(output_path):
        os.remove(output_path)
    result = runner.invoke(
        app, ["write-daily-rain-plot", "--data-path", data_path, "--output-path", output_path]
    )
    assert result.exit_code == 0
    assert os.path.isfile(output_path)


def test_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "0.1.0" in result.stdout
