from tabulate import tabulate
from rich.console import Console
import sys

def dynamic_import_run_crew():
    from financial_analyst_crew.financial_analyst import cli_prompt
    cli_prompt()
    main_menu()  # Call main_menu again after running the crew

def main_menu():
    console = Console()
    console.print("[bold magenta]CrewAI Application Overview[/bold magenta]", justify="center")
    console.print("This application showcases the capabilities of CrewAI in orchestrating AI-driven solutions through agent-based delivery.", justify="center")
    console.print("\nChoose from one of the options below to get started.", justify="center")

    menu_options = [
        ["1", "Financial Analyst Crew", "Demonstrates stock research using Company Researcher and Company Analyst agents"],
        ["99", "Exit", "Exit the application"]
    ]

    console.print(tabulate(menu_options, headers=["Option", "Crew", "Description"], tablefmt="grid"))

    try:
        choice = int(console.input("[bold green]Enter your choice: [/bold green]"))
        if choice == 1:
            dynamic_import_run_crew()
        elif choice == 99:
            sys.exit("Exiting the application...")
        else:
            console.print("[bold red]Invalid option, please try again.[/bold red]")
            main_menu()
    except ValueError:
        console.print("[bold red]Please enter a valid number.[/bold red]")
        main_menu()

if __name__ == "__main__":
    main_menu()
