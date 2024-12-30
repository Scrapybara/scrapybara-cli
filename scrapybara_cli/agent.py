from scrapybara_cli.prompt import SYSTEM_PROMPT
from scrapybara_cli.helpers import ToolCollection, make_tool_result
from scrapybara.client import Instance
from anthropic import Anthropic
from rich import print
from rich.live import Live
from rich.text import Text
from rich.panel import Panel


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
        # Process tool usage
        tool_results = []
        for content in response.content:
            if content.type == "text":
                print(content.text)
            elif content.type == "tool_use":
                with Live(auto_refresh=False) as live:
                    live.update(
                        Panel(
                            Text.from_markup(
                                f"[bold blue]Running {content.name} with {content.input}[/bold blue]"
                            )
                        )
                    )

                    result = await tools.run(
                        name=content.name, tool_input=content.input  # type: ignore
                    )

                    if content.name == "bash" and not result:
                        result = await tools.run(
                            name="computer", tool_input={"action": "screenshot"}
                        )

                    if result:
                        tool_result = make_tool_result(result, content.id)
                        tool_results.append(tool_result)

                        if result.output:
                            live.update(
                                Panel(
                                    Text.from_markup(
                                        f"[bold green]Tool Output: {result.output}[/bold green]"
                                    )
                                )
                            )
                        if result.error:
                            live.update(
                                Panel(
                                    Text.from_markup(
                                        f"[bold red]Tool Error: {result.error}[/bold red]"
                                    )
                                )
                            )

        # Add assistant's response and tool results to messages
        messages.append(
            {"role": "assistant", "content": [c.model_dump() for c in response.content]}
        )

        if tool_results:
            messages.append({"role": "user", "content": tool_results})
        else:
            break
