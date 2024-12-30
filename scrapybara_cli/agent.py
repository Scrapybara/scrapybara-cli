from .prompt import SYSTEM_PROMPT
from .helpers import ToolCollection, make_tool_result
from scrapybara.client import Instance
from anthropic import Anthropic
from rich import print


async def run_agent(instance: Instance, tools: ToolCollection, prompt: str) -> None:
    anthropic = Anthropic()

    messages = []
    messages.append({"role": "user", "content": [{"type": "text", "text": prompt}]})

    while True:
        # Get Claude's response
        response = anthropic.beta.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4096,
            messages=messages,
            system=[{"type": "text", "text": SYSTEM_PROMPT}],
            tools=tools.to_params(),
            betas=["computer-use-2024-10-22"],
        )

        # Process tool usage
        tool_results = []
        for content in response.content:
            if content.type == "text":
                print(content.text)
            elif content.type == "tool_use":
                text = f"Running {content.name} with {content.input}"

                if content.name == "computer":
                    if content.input["action"] == "screenshot":  # type: ignore
                        text = "Taking screenshot"
                    elif content.input["action"] == "left_click" or content.input["action"] == "right_click":  # type: ignore
                        text = "Clicking"
                    elif content.input["action"] == "type":  # type: ignore
                        text = "Typing"
                    elif content.input["action"] == "scroll":  # type: ignore
                        text = "Scrolling"
                    elif content.input["action"] == "key":  # type: ignore
                        text = f"Pressing key {content.input['text']}"  # type: ignore
                    elif content.input["action"] == "mouse_move":  # type: ignore
                        text = "Moving mouse"

                if content.name == "bash":
                    text = f"$ {content.input['command']}"  # type: ignore

                print(f"[bold blue]{text}[/bold blue]")

                result = await tools.run(
                    name=content.name, tool_input=content.input  # type: ignore
                )

                tool_result = make_tool_result(result, content.id)
                tool_results.append(tool_result)

                if result.output:
                    print(f"[bold green]{result.output}[/bold green]")
                if result.error:
                    print(f"[bold red]{result.error}[/bold red]")

        # Add assistant's response and tool results to messages
        messages.append(
            {"role": "assistant", "content": [c.model_dump() for c in response.content]}
        )

        if tool_results:
            messages.append({"role": "user", "content": tool_results})
        else:
            break
