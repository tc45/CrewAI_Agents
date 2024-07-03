from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI


# noinspection PyTypeChecker
@CrewBase
class FinancialAnalystCrew:
    """FinancialAnalystCrew crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self) -> None:
        self.tasks = None
        self.agents = None
        self.groq_llm = ChatGroq(temperature=0, model_name="llama3-70b-8192")
        self.openai_llm = ChatOpenAI(base_url='http://localhost:1234/v1', api_key="lm_studio")

    @agent
    def company_researcher(self) -> Agent:
        company_researcher = self.agents_config['company_researcher']
        company_analyst = self.agents_config['company_analyst']
        research_company_task = self.tasks_config['research_company_task']
        analyze_company_task = self.tasks_config['analyze_company_task']

        return Agent(
            config=self.agents_config['company_researcher'],
            # llm=self.groq_llm
            llm=self.openai_llm
        )


    @agent
    def company_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['company_analyst'],
            llm=self.groq_llm
        )

    @task
    def research_company_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_company_task'],
            agent=self.company_researcher()
        )

    @task
    def analyze_company_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_company_task'],
            agent=self.company_analyst()
        )

    @crew
    def crew(self) -> Crew:
        """Create the FinancialAnalystCrew crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=2,
        )
