from getpass import getpass
import os
import typer


def check_required_keys():
    """Check and prompt for required API keys if not present in environment"""
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
