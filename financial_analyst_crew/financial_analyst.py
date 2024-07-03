from financial_analyst_crew.crew import FinancialAnalystCrew
from dotenv import load_dotenv

load_dotenv()


def run():
    inputs = {
        'company_name': 'Tesla',
    }
    response = FinancialAnalystCrew().crew().kickoff(inputs=inputs)
    print(response)


if __name__ == "__main__":
    run()
