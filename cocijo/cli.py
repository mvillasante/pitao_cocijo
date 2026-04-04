import cocijo
import typer

app = typer.Typer()


@app.command()
def version():
    print(cocijo.__version__)
