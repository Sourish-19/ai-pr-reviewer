# section 4: cli.py
# Person 4 can explain this section

import typer
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from typing import Optional

# Setup Typer App and Rich Console
app = typer.Typer(help="AI PR Review CLI - Automated Pull Request reviewer")
console = Console()

class CLIInterface:
    def __init__(self):
        self.console = console

    def display_welcome(self):
        self.console.print(Panel.fit(
            "[bold blue]AI PR Review CLI[/bold blue]\n"
            "Automatically review GitHub PRs for quality, security, and integration.",
            border_style="cyan"
        ))

    def show_spinner(self, message: str):
        """
        Returns a context manager for a loading spinner.
        """
        return self.console.status(f"[bold yellow]{message}[/bold yellow]")

    def display_results(self, parsed_review: dict):
        """
        Renders the structured review nicely in the terminal.
        """
        self.console.print("\n[bold green]✅ Review Complete![/bold green]\n")
        
        categories = ["Code Quality", "Security", "Codebase Integration"]
        colors = {"Code Quality": "blue", "Security": "red", "Codebase Integration": "magenta"}

        for category in categories:
            content = parsed_review.get(category, "No report.")
            
            # If the parser couldn't find the sections, fallback to just displaying raw text
            if content == "No report." and category == "Code Quality" and "Raw" in parsed_review:
                 # Fallback strategy
                 self.console.print(Panel(Markdown(parsed_review["Raw"]), title="[bold white]Full AI Review[/bold white]"))
                 break

            self.console.print(Panel(
                Markdown(content), 
                title=f"[bold {colors[category]}]{category}[/bold {colors[category]}]", 
                border_style=colors[category]
            ))
            self.console.print()

    def display_error(self, message: str):
        self.console.print(f"[bold red]❌ Error:[/bold red] {message}")
