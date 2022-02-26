"""CLI tool for listing (un)available AWS services by region."""

from typing import Optional

from enum import Enum
from random import choice

import typer
from rich.console import Console

from aws_service_availability import version
from aws_service_availability.example import hello


class Color(str, Enum):
    """Enum of CLI output colors."""

    WHITE = "white"
    RED = "red"
    CYAN = "cyan"
    MAGENTA = "magenta"
    YELLOW = "yellow"
    GREEN = "green"


app = typer.Typer(
    name="aws-service-availability",
    help="CLI tool for listing (un)available AWS services by region",
    add_completion=False,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]aws-service-availability[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


@app.command(name="")
def main(
    name: str = typer.Option(..., help="Person to greet."),
    color: Optional[Color] = typer.Option(
        None,
        "-c",
        "--color",
        "--colour",
        case_sensitive=False,
        help="Color for print. If not specified then choice will be random.",
    ),
    print_version: bool = typer.Option(  # pylint: disable=unused-argument
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the aws-service-availability package.",
    ),
) -> None:
    """Print a greeting with a given name."""
    if color is None:
        color = choice(list(Color))  # nosec - PRNG is not used for a cryptographic purpose

    greeting: str = hello(name)
    console.print(f"[bold {color}]{greeting}[/]")


if __name__ == "__main__":
    app()
