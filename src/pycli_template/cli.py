import time
import typer

from rich.progress import track


cli = typer.Typer()


@cli.command()
def greet(name: str = "World"):
    """Greet the user."""
    typer.echo(f"Hello, {name}!")


@cli.command()
def init():
    """Initialize the project."""
    progess = 0
    for _ in track(range(100), description="Initializing..."):
        time.sleep(0.05)
        progess += 1
    typer.echo("Project initialized successfully!")
