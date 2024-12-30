from scrapybara_cli.prompt import SYSTEM_PROMPT
from scrapybara_cli.helpers import ToolCollection, make_tool_result
from scrapybara.client import Instance
from anthropic import Anthropic


def run_agent(instance: Instance, tools: ToolCollection, prompt: str):
    anthropic = Anthropic()

    messages = []
    messages.append({"role": "user", "content": [{"type": "text", "text": prompt}]})
