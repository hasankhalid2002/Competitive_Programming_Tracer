import sys
from core.fetcher import CodeforcesFetcher
from core.analyzer import CodeforcesAnalyzer
from core.exceptions import CPTracerException
from ui.presenter import CLIPresenter

def main():
    presenter = CLIPresenter()
    fetcher = CodeforcesFetcher()

    # 1. Reading the user's Handle
    if len(sys.argv) > 1:
        handle = sys.argv[1]
    else:
        handle = input("Enter Codeforces Handle: ").strip()

    if not handle:
        presenter.print_error("Handle cannot be empty!")
        return

    # 2. collecting data and analyzing with error handling
    try:
        presenter.console.print(f"[yellow]Fetching data for '{handle}'...[/yellow]")
        
        # Fetching
        user_profile = fetcher.fetch_user_profile(handle)
        submissions = fetcher.fetch_user_submissions(handle)
        
        # Analyzing
        analyzer = CodeforcesAnalyzer(submissions)

        # Presenting Results
        presenter.console.print("[green]Data fetched successfully![/green]\n")
        presenter.print_user_header(user_profile)
        presenter.print_analytics(analyzer)

    except CPTracerException as e:
        presenter.print_error(str(e))
    except Exception as e:
        presenter.print_error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
