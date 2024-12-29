import typer
from scrapybara import Scrapybara
from dotenv import load_dotenv
from rich.console import Console
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
        with console.status("[bold green]Starting instance...", spinner="dots") as status:
            instance = scrapybara.start(instance_type=instance_type)
            status.update("[bold green]Instance started!")

    finally:
        with console.status("[bold red]Stopping instance...", spinner="dots") as status:
            instance.stop()
            status.update("[bold red]Instance stopped!")
    

if __name__ == "__main__":
    typer.run(main)