from cocijo.plot_series import plot_yearly_rain, plot_cumulative_yearly_rain
import cocijo

import matplotlib
import pandas as pd
import typer

app = typer.Typer()


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
