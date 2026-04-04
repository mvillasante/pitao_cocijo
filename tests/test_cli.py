from cocijo.cli import app
from typer.testing import CliRunner

runner = CliRunner()


def test_write_daily_rain():
    result = runner.invoke(app, ["write-daily-rain-plot", "--help"])
    assert result.exit_code == 0
    data_path = "tests/data/registro_lluvias_for_test.csv"
    output_path = "tests/data/lluvia_diaria.png"

    result = runner.invoke(
        app, ["write-daily-rain-plot", "data-path", data_path, "output-path", output_path]
    )
    assert result.exit_code == 0


def test_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "0.1.0" in result.stdout
