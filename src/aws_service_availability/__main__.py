"""CLI tool for listing (un)available AWS services by region."""

import typer
from rich.console import Console

from aws_service_availability.scraper import AwsServiceAvailability

app = typer.Typer(
    name="aws-service-availability",
    help="CLI tool for listing (un)available AWS services by region",
    add_completion=False,
)
console = Console()


@app.command(name="list-unsupported-services")
def list_unsupported(
    region: str = typer.Argument(..., help="AWS Region."),
) -> None:
    """Print a list of unsupported AWS services for the region."""
    scraper = AwsServiceAvailability()
    unsupported_services = scraper.get_unsupported_services(region)
    if unsupported_services:
        console.print(
            f"[bold yellow]{len(unsupported_services)}[/] unsupported AWS services for region [bold blue]{region}[/]:"
        )
        for service in unsupported_services:
            console.print(f" - [bold red]{service}[/]")


@app.command(name="list-supported-services")
def list_supported(
    region: str = typer.Argument(..., help="AWS Region."),
) -> None:
    """Print a list of supported AWS services for the region."""
    scraper = AwsServiceAvailability()
    supported_services = scraper.get_supported_services(region)
    if supported_services:
        console.print(
            f"[bold yellow]{len(supported_services)}[/] supported AWS services for region [bold blue]{region}[/]:"
        )
        for service in supported_services:
            console.print(f" - [bold green]{service}[/]")


if __name__ == "__main__":
    app()
