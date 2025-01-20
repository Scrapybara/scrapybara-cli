from rich import print
from scrapybara.types.act import Step


def print_step(step: Step):
    """Print step information with clean formatting"""
    # Print assistant's message if not empty
    if step.text and step.text.strip():
        print(f"\n{step.text}")

    # Print tool executions
    if step.tool_calls:
        for tool_call in step.tool_calls:
            match tool_call.tool_name:
                case "computer":
                    action = tool_call.args.get("action")
                    match action:
                        case "screenshot":
                            print("[yellow]Screenshot[/yellow]")
                        case "mouse_move":
                            print("[yellow]Moving mouse[/yellow]")
                        case "scroll":
                            print("[yellow]Scrolling[/yellow]")
                        case "left_click" | "right_click":
                            print("[yellow]Clicking[/yellow]")
                        case "type":
                            text = tool_call.args.get("text", "").strip()
                            if text:
                                print(f"[yellow]Typing:[/yellow] {text}")
                            else:
                                print("[yellow]Typing[/yellow]")
                        case "key":
                            print(
                                f"[yellow]Pressing key '{tool_call.args['text'].upper()}'[/yellow]"
                            )
                case "bash":
                    cmd = tool_call.args.get("command", "").strip()
                    if cmd:
                        print(f"[yellow](instance) $ {cmd}[/yellow]")

    # Print non-empty tool results
    if step.tool_results:
        for result in step.tool_results:
            if result.result and str(result.result).strip():
                match result.tool_name:
                    case "computer":
                        pass
                    case "bash":
                        if (
                            result.result["output"] != ""
                            and result.is_error is False
                        ):
                            print(f"[green]{result.result['output']}[/green]")
                        elif (
                            result.result["output"] != ""
                            and result.is_error is True
                        ):
                            print(f"[red]{result.result['output']}[/red]")

