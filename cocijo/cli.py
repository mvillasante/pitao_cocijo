from cocijo.plot_series import plot_yearly_rain, plot_cumulative_yearly_rain
from cocijo.summary import get_five_numbers, render_template

import cocijo

import matplotlib
import pandas as pd
import typer

app = typer.Typer()


@app.command()
def update_readme(
    data_path: str = typer.Option(),
    template_path: str = typer.Option(),
    output_path: str = typer.Option(),
):
    data = pd.read_csv(data_path)
    summary = get_five_numbers(data)
    template_with_summary = render_template(template_path, summary)
    with open(output_path, "w") as doc:
        doc.writelines(template_with_summary + "\n")


@app.command()
def write_cumulative_rain_plot(data_path: str = typer.Option(), output_path: str = typer.Option()):
    data = pd.read_csv(data_path)
    plot_cumulative_yearly_rain(data)
    matplotlib.pyplot.savefig(output_path)


@app.command()
def write_daily_rain_plot(data_path: str = typer.Option(), output_path: str = typer.Option()):
    data = pd.read_csv(data_path)
    plot_yearly_rain(data)
    matplotlib.pyplot.savefig(output_path)


@app.command()
def version():
    print(cocijo.__version__)
