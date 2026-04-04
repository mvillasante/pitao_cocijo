import cocijo
import typer

app = typer.Typer()


@app.command()
def write_daily_rain_plot():
    pass


@app.command()
def version():
    print(cocijo.__version__)
