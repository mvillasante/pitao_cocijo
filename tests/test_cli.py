from cocijo.cli import app
from typer.testing import CliRunner

runner = CliRunner()


def test_app_write_monthly_summary():
    result = runner.invoke(
        app,
        ["version"],
    )
    assert result.exit_code == 0
    assert "0.1.0" in result.stdout
