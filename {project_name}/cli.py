import click


@click.group()
def cli():
    pass


@cli.command()
@click.option("--name", default="World", help="Name to greet")
def greet(name):
    """Greet the user."""
    click.echo(f"Hello, {name}!")
