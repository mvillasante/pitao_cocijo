from cocijo.cli import app
from typer.testing import CliRunner

runner = CliRunner()


def test_write_daily_rain():
    result = runner.invoke(app, ["write-daily-rain-plot", "--help"])
    assert result.exit_code == 0


def test_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "0.1.0" in result.stdout
