import typer
from scrapybara import Scrapybara
from dotenv import load_dotenv
from rich.console import Console
from rich import print
import os

load_dotenv()

console = Console()
scrapybara = Scrapybara(api_key=os.getenv("SCRAPYBARA_API_KEY"))

def main(instance_type: str = "small"):
    """
    Run the CLI-based computer agent, powered by Scrapybara and Anthropic!
    
    Args:
        instance_type: Size of the instance. Must be one of: "small", "medium", "large"
    """
    if instance_type not in ["small", "medium", "large"]:
        raise ValueError('instance_type must be one of: "small", "medium", "large"')
    
    try:
        with console.status("[bold green]Starting instance...[/bold green]", spinner="dots") as status:
            instance = scrapybara.start(instance_type=instance_type)
            status.update("[bold green]Instance started![/bold green]")

        stream_url = instance.get_stream_url().stream_url
        print(f"[bold blue]Stream URL: {stream_url}[/bold blue]")

        while True:
            prompt = input("> ")
            if prompt == "exit":
                break
            else:
                print(f"[bold blue]Prompt: {prompt}[/bold blue]")

    except KeyboardInterrupt:
        pass

    finally:
        with console.status("[bold red]Stopping instance...[/bold red]", spinner="dots") as status:
            instance.stop()
            status.update("[bold red]Instance stopped![/bold red]")
    

if __name__ == "__main__":
    typer.run(main)