# CrewAI Project Documentation

This project demonstrates the versatility and power of CrewAI in orchestrating AI-driven solutions through agent-based delivery. Below is a consolidated overview of CrewAI, installation instructions, execution guidance, and a detailed look into one of its specific applications: the Financial Analyst Crew.

## Table of Contents
- [Overview](#overview)
- [Install and Execution](#install-and-execution)
- [Financial Analyst Crew](#financial-analyst-crew)
- [Conclusion](#conclusion)

## Overview

CrewAI is a pioneering framework in the AI landscape, designed to streamline complex operations through the orchestration of autonomous agents. It combines simplicity with efficiency, making it suitable for a wide range of engineering applications. By leveraging collaborative intelligence, CrewAI enables these agents, each with their unique roles and capabilities, to work together seamlessly. The integration with LangChain further enhances its versatility, allowing for the development of agents capable of tackling everything from routine tasks to intricate analyses, thereby broadening the scope of potential applications.

This project is provided to demonstrate simple use cases of CrewAI using my known best practices at the time of writing.  This is a proof of concept, and should not be used in any production like settings.
## Install and Execution

To get started with the CrewAI project, follow these generic instructions:

### Cloning the Repository

1. Open your terminal or command prompt.
2. Clone the repository using Git:

```bash
git clone https://github.com/your-repository/CrewAI.git
```

3. Navigate to the cloned repository's directory:
```bash
cd CrewAI_Agents
```
### Updating the .env File

After cloning the repository and before running the Financial Analyst Crew, it's essential to configure your environment variables. This involves updating the `.env` file with your API keys and URLs for the services the crew will interact with. Specifically, you need to provide values for `GROQ_API_KEY`, `OPENAI_API_KEY`, and `OPENAI_BASE_URL`. These keys enable the CrewAI agents to access the necessary language model APIs for performing tasks.

1. Create a `.env` file in the root directory of the cloned repository.
2. Open the `.env` file in a text editor.
3. update the following lines with your actual API keys and URL:
   - GROQ_API_KEY
   - OPENAI_API_KEY
   - OPENAI_BASE_URL (Leave blank to connect directly to OpenAI, or overwrite with custom URL for other URLs.)
4. Save the changes to the `.env` file.

These steps ensure that your instance of the Financial Analyst Crew has the necessary credentials to access GROQ and OpenAI services, allowing for the successful execution of its tasks.

### Installing Dependencies

4. Ensure you have Python installed on your system.
5. Install the required dependencies by running:
```bash
pip install -r requirements.txt
```

### Running the main application

1. Run main.py and follow the menu system.
```bash
python main.py
```

## Financial Analyst Crew

The Financial Analyst Crew exemplifies the practical application of CrewAI in the domain of financial analysis. This crew employs two distinct types of agents, each with specific roles and tasks, to conduct an in-depth analysis of companies.

### Running the script
When this script is run, it will prompt you for the name of a company to do research on.  Enter the name, and let the LLMs do the hard work.
### Agents

#### Company Researcher
- **Role**: Financial Researcher
- **Goal**: To gather all necessary financial information about a company using search tools, preparing the groundwork for the financial analyst.
- **Backstory**: An expert financial researcher dedicated to understanding the financial performance of various companies.
- **Characteristics**: Does not delegate tasks and operates with high verbosity, ensuring detailed and comprehensive research output.

#### Company Analyst
- **Role**: Financial Analyst
- **Goal**: To analyze the provided financial information and create a detailed financial report on a given company.
- **Backstory**: A seasoned financial researcher known for producing clear, concise, and informative financial reports.
- **Characteristics**: Works independently without delegating tasks and communicates findings effectively.

### Tasks

#### Research Company Task
- **Description**: Utilizes search tools to gather stock information about a specified company (`{company_name}`). The objective is to compile sufficient data for an informed analysis of the company's stock performance.
- **Expected Output**: A compilation of relevant financial data concerning the company's stock performance, ready for analysis.

#### Analyze Company Task
- **Description**: Analyzes the financial information of `{company_name}`, focusing on various financial metrics such as profitability ratios, liquidity ratios, solvency ratios, efficiency ratios, growth metrics, valuation metrics, and cash flow.
- **Expected Output**: A comprehensive financial analysis report, neatly formatted to include all necessary financial metrics for a thorough evaluation of the company.

## Conclusion

The Financial Analyst Crew, powered by CrewAI, demonstrates the framework's capability to facilitate complex analytical tasks through the collaboration of specialized AI agents. By dividing the workflow into distinct research and analysis phases, the crew efficiently processes and analyzes financial data, resulting in actionable insights into a company's financial health. This approach not only streamlines the analysis process but also leverages the unique strengths and expertise of each agent, showcasing the potential of agent-based AI in financial analysis.

