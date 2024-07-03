from financial_analyst_crew.crew import FinancialAnalystCrew
from dotenv import load_dotenv
from rich.console import Console

load_dotenv()


def run_crew(company_name):
    """
    Executes the main logic to analyze a specified company using the FinancialAnalystCrew.

    Creates an instance of FinancialAnalystCrew, kicks off the analysis with given inputs,
    and prints the response.
    """
    # Define inputs for the analysis task.
    inputs = {
        'company_name': company_name,
    }
    # Create an instance of FinancialAnalystCrew, kickoff the analysis, and capture the response.
    response = FinancialAnalystCrew().crew().kickoff(inputs=inputs)
    # Print the analysis response.
    print(response)
    print("\n\n\n\n\n")


def cli_prompt():
    """
    Prompts the user for a company name or ticker symbol and calls run_crew with the input.
    """
    console = Console()
    console.print("[bold magenta]Financial Analyst Crew Overview[/bold magenta]", justify="center")
    console.print("The Financial Analyst Crew utilizes two agents: [bold]Company Researcher[/bold] and [bold]Company Analyst[/bold].", justify="left")
    console.print("Tasks include researching a company's financial data and analyzing this information to generate insights.", justify="left")
    console.print("\nPlease enter the company name or ticker symbol (prefix with $) you wish to analyze. Default is Microsoft.", justify="left")

    # Prompt for company name or ticker symbol, default to 'Microsoft' if no input is given.
    company_input = console.input("[bold green]Company Name/Ticker Symbol: [/bold green]") or "Microsoft"
    # Remove '$' if input is a ticker symbol.
    company_name = company_input.lstrip('$')

    run_crew(company_name)

if __name__ == "__main__":
    cli_prompt()
