from prompt import SYSTEM_PROMPT
from helpers import ToolCollection, make_tool_result
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
                text = f"[bold blue]Running {content.name} with {content.input}[/bold blue]"

                if content.name == "computer":
                    if content.input["action"] == "screenshot":  # type: ignore
                        text = f"[bold blue]Taking screenshot[/bold blue]"
                    elif content.input["action"] == "left_click" or content.input["action"] == "right_click":  # type: ignore
                        text = f"[bold blue]Clicking[/bold blue]"
                    elif content.input["action"] == "type":  # type: ignore
                        text = f"[bold blue]Typing[/bold blue]"
                    elif content.input["action"] == "scroll":  # type: ignore
                        text = f"[bold blue]Scrolling[/bold blue]"
                    elif content.input["action"] == "key":  # type: ignore
                        text = f"[bold blue]Pressing key {content.input['text']}[/bold blue]"  # type: ignore
                    elif content.input["action"] == "mouse_move":  # type: ignore
                        text = f"[bold blue]Moving mouse[/bold blue]"

                if content.name == "bash":
                    text = f"[bold blue]$ {content.input['command']}[/bold blue]"  # type: ignore

                print(text)

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
