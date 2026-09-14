from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from models.user import UserProfile
from core.analyzer import CodeforcesAnalyzer

class CLIPresenter:
    def __init__(self):
        self.console = Console()

    def print_user_header(self, profile: UserProfile):
        title = f"[bold cyan]{profile.handle}[/bold cyan] ({profile.rank})"
        content = (
            f"Rating: [bold green]{profile.rating}[/bold green] (Max: {profile.max_rating})\n"
            f"Rank: [bold yellow]{profile.rank}[/bold yellow]"
        )
        self.console.print(Panel(content, title=title, expand=False))

    def print_analytics(self, analyzer: CodeforcesAnalyzer):
        acc_rate = analyzer.get_acceptance_rate()
        self.console.print(f"\n[bold]Acceptance Rate:[/bold] [bold magenta]{acc_rate}%[/bold magenta]\n")

        # Table 1: Verdict Breakdown
        verdict_table = Table(title="Submissions Breakdown")
        verdict_table.add_column("Verdict", style="cyan")
        verdict_table.add_column("Count", style="green", justify="right")

        for verdict, count in analyzer.get_verdict_stats().items():
            verdict_table.add_row(verdict, str(count))
        self.console.print(verdict_table)

        # Table 2: Top Tags
        tag_table = Table(title="Top Solved Topics (Tags)")
        tag_table.add_column("Topic / Tag", style="yellow")
        tag_table.add_column("Problems Solved", style="green", justify="right")

        top_tags = sorted(analyzer.get_tag_distribution().items(), key=lambda x: x[1], reverse=True)[:10]
        for tag, count in top_tags:
            tag_table.add_row(tag, str(count))
        self.console.print(tag_table)

        # Table 3: Rating Distribution
        rating_table = Table(title="Difficulty Rating Distribution")
        rating_table.add_column("Problem Rating", style="blue")
        rating_table.add_column("Solved Count", style="green", justify="right")

        for rating, count in analyzer.get_rating_distribution().items():
            rating_table.add_row(str(rating), str(count))
        self.console.print(rating_table)

    def print_error(self, message: str):
        self.console.print(f"[bold red]Error:[/bold red] {message}")