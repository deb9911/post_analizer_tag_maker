from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.models.google import gemini
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools
import json

config_dir = "./agent_config.json"
log_dir = './agent_log/agno_class1.log'


def load_agent_config(config_path):
    if not config_path:
        print('Error config path')
        return {}
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except Exception as config_read_error:
        print(f'Exception has happened while reading config file at==> \t{config_read_error.args}')
        return {}


def financial_agent_class1(company_name):
    config = load_agent_config(config_dir)
    custom_prompt = f"Writing report on financial analysis on {company_name}"
    gemini_api_key = config['gemini_api_key']
    model = gemini.Gemini(api_key=gemini_api_key)

    agent = Agent(
        model=model,
        tools=[
            YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True),
            ReasoningTools
        ],
        instructions=[
            "Use table to display data",
            "Respond with only repost, not any other data"
        ],
        markdown=True
    )
    try:
        agent.print_response(message=custom_prompt,
                             stream=True,
                             show_full_reasoning=True,
                             stream_intermediate_steps=True
                             )
    except Exception as agent_error:
        print(f'Getting error while try to fetch target entity as ==>{agent_error.args}')


if __name__ == '__main__':
    target_company = input('Enter the company to get financial details through this Agentic Model==>#\t')
    financial_agent_class1(target_company)

