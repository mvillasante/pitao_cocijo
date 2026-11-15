from cocijo.cli import app
from typer.testing import CliRunner
import os

runner = CliRunner()


data_path = "tests/data/registro_lluvias_for_test.csv"


def test_update_readme():
    command = "update-readme"
    result = runner.invoke(app, [command, "--help"])
    assert result.exit_code == 0

    template_path = "tests/data/README_for_tests.md"
    output_path = "tests/README_rellenado.md"

    if_exist_remove(output_path)
    result = runner.invoke(
        app,
        [
            command,
            "--data-path",
            data_path,
            "--template-path",
            template_path,
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    assert os.path.isfile(output_path)


def test_write_cumulative_rain():
    result = runner.invoke(app, ["write-cumulative-rain-plot", "--help"])
    assert result.exit_code == 0
    output_path = "tests/data/lluvia_acumulada.png"

    if_exist_remove(output_path)
    result = runner.invoke(
        app, ["write-cumulative-rain-plot", "--data-path", data_path, "--output-path", output_path]
    )
    assert result.exit_code == 0
    assert os.path.isfile(output_path)
    if_exist_remove(output_path)


def test_write_daily_rain():
    result = runner.invoke(app, ["write-daily-rain-plot", "--help"])
    assert result.exit_code == 0
    output_path = "tests/data/lluvia_diaria.png"

    if_exist_remove(output_path)
    result = runner.invoke(
        app, ["write-daily-rain-plot", "--data-path", data_path, "--output-path", output_path]
    )
    assert result.exit_code == 0
    assert os.path.isfile(output_path)
    if_exist_remove(output_path)


def test_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "0.1.0" in result.stdout


def if_exist_remove(output_path):
    if os.path.isfile(output_path):
        os.remove(output_path)
