from scrapybara.tools import ComputerTool, BashTool, EditTool
from scrapybara.prompts import SYSTEM_PROMPT
from scrapybara.anthropic import Anthropic
from scrapybara import Scrapybara
from dotenv import load_dotenv
from rich.console import Console
from rich import print
from .callback import print_step
from getpass import getpass
import typer
import os

load_dotenv()

console = Console()
app = typer.Typer()


@app.command()
def main(
    instance_type: str = typer.Option(
        "small", help="Size of the instance. Must be one of: 'small', 'medium', 'large'"
    )
):
    """
    Run the CLI-based computer agent, powered by Scrapybara and Anthropic!
    """
    if instance_type not in ["small", "medium", "large"]:
        raise typer.BadParameter(
            'instance_type must be one of: "small", "medium", "large"'
        )

    if not os.getenv("SCRAPYBARA_API_KEY"):
        scrapybara_key = getpass("Please enter your Scrapybara API key: ").strip()
        if not scrapybara_key:
            raise typer.BadParameter("Scrapybara API key is required to continue.")
        os.environ["SCRAPYBARA_API_KEY"] = scrapybara_key

    if not os.getenv("ANTHROPIC_API_KEY"):
        anthropic_key = getpass("Please enter your Anthropic API key: ").strip()
        if not anthropic_key:
            raise typer.BadParameter("Anthropic API key is required to continue.")
        os.environ["ANTHROPIC_API_KEY"] = anthropic_key

    client = Scrapybara(api_key=os.getenv("SCRAPYBARA_API_KEY"))

    try:
        with console.status(
            "[bold green]Starting instance...[/bold green]", spinner="dots"
        ) as status:
            instance = client.start(instance_type=instance_type)
            status.update("[bold green]Instance started![/bold green]")

        stream_url = instance.get_stream_url().stream_url
        print(
            f"[bold blue]Stream URL: {stream_url}/?resize=scale&autoconnect=1[/bold blue]"
        )

        while True:
            prompt = input("> ")

            try:
                client.act(
                    model=Anthropic(),
                    tools=[
                    ComputerTool(instance),
                    BashTool(instance),
                    EditTool(instance),
                ],
                system=SYSTEM_PROMPT,
                prompt=prompt,
                on_step=print_step,
            )

            except UnboundLocalError as e:
                pass  # Make this shit shut up until Justin fixes

    except Exception as e:
        print(f"[bold red]{e}[/bold red]")

    finally:
        with console.status(
            "[bold red]Stopping instance...[/bold red]", spinner="dots"
        ) as status:
            instance.stop()
            status.update("[bold red]Instance stopped![/bold red]")


if __name__ == "__main__":
    app()
