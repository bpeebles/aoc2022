import importlib

import typer

app = typer.Typer()


@app.command()
def day1(src: str = "", part: str = "1"):
    import day1
    if part == "1":
        day1.part1(src)
    if part == "2":
        day1.part2(src)


@app.command()
def day2(src: str):
    pass

if __name__ == "__main__":
    app()
