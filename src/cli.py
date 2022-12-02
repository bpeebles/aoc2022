import importlib

import typer

app = typer.Typer()


@app.command()
def day1(src: str = ""):
    import day1
    day1.run(src)


@app.command()
def day2(src: str):
    pass

if __name__ == "__main__":
    app()
