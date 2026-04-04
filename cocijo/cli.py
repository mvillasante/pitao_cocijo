import typer

app = typer.Typer()


@app.command()
def version():
    print("0.1.0")
