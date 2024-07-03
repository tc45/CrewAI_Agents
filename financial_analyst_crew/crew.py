from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI


# noinspection PyTypeChecker
@CrewBase
class FinancialAnalystCrew:
    """
    Defines a crew specialized in financial analysis tasks.

    Attributes:
        agents_config (str): Path to the YAML configuration file for agents.
        tasks_config (str): Path to the YAML configuration file for tasks.
        tasks (NoneType): Placeholder for tasks, to be initialized later.
        agents (NoneType): Placeholder for agents, to be initialized later.
        groq_llm (ChatGroq): Instance of ChatGroq for language model interactions.
        openai_llm (ChatOpenAI): Instance of ChatOpenAI for language model interactions.
    """
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self) -> None:
        """Initializes the FinancialAnalystCrew with specific language models."""
        self.tasks = None
        self.agents = None
        # Initialize ChatGroq with specific parameters.
        self.groq_llm = ChatGroq(temperature=0, model_name="llama3-70b-8192")
        # Initialize ChatOpenAI with specific parameters.
        self.openai_llm = ChatOpenAI(base_url='http://localhost:1234/v1', api_key="lm_studio")

    @agent
    def company_researcher(self) -> Agent:
        """
        Defines the company researcher agent.

        Returns:
            Agent: Configured agent instance for company research.
        """
        # Configuration for company researcher and analyst agents.
        company_researcher = self.agents_config['company_researcher']
        company_analyst = self.agents_config['company_analyst']
        # Configuration for research and analyze company tasks.
        research_company_task = self.tasks_config['research_company_task']
        analyze_company_task = self.tasks_config['analyze_company_task']

        # Return an Agent instance configured for company research.
        return Agent(
            config=self.agents_config['company_researcher'],
            llm=self.groq_llm
            #llm=self.openai_llm
        )

    @agent
    def company_analyst(self) -> Agent:
        """
        Defines the company analyst agent.

        Returns:
            Agent: Configured agent instance for company analysis.
        """
        return Agent(
            config=self.agents_config['company_analyst'],
            llm=self.groq_llm
        )

    @task
    def research_company_task(self) -> Task:
        """
        Defines the task for researching a company.

        Returns:
            Task: Configured task instance for researching a company.
        """
        return Task(
            config=self.tasks_config['research_company_task'],
            agent=self.company_researcher()
        )

    @task
    def analyze_company_task(self) -> Task:
        """
        Defines the task for analyzing a company.

        Returns:
            Task: Configured task instance for analyzing a company.
        """
        return Task(
            config=self.tasks_config['analyze_company_task'],
            agent=self.company_analyst()
        )

    @crew
    def crew(self) -> Crew:
        """
        Creates and returns the FinancialAnalystCrew.

        Returns:
            Crew: The configured crew instance for financial analysis.
        """
        # Create and return a Crew instance with sequential processing.
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=2,
        )
