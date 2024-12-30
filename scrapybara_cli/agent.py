from scrapybara_cli.prompt import SYSTEM_PROMPT
from scrapybara_cli.helpers import ToolCollection, make_tool_result
from scrapybara.client import Instance
from anthropic import Anthropic


async def run_agent(instance: Instance, tools: ToolCollection, prompt: str):
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
                # logger.info(f"Assistant: {content.text}")
                pass
            elif content.type == "tool_use":
                # logger.info(f"Running tool: {content.name}")
                # logger.info(f"Tool input: {content.input}")
                result = await tools.run(name=content.name, tool_input=content.input)  # type: ignore

                if result:
                    if result.output:
                        # logger.info(f"Tool output: {result.output}")
                        pass
                    tool_result = make_tool_result(result, content.id)
                    tool_results.append(tool_result)

        # Add assistant's response and tool results to messages
        messages.append(
            {"role": "assistant", "content": [c.model_dump() for c in response.content]}
        )

        if tool_results:
            messages.append({"role": "user", "content": tool_results})
        else:
            break

    return messages
