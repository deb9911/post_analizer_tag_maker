from agno.agent import Agent
from agno.models.google import gemini
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools
import json

config_dir = "./agent_config.json"
log_dir = './agent_log/agno_class1.log'


class ConfigLoader:
    @staticmethod
    def loading_agent_config(config_path):
        if not config_path:
            return {}
        try:
            with open(config_path, "r") as f:
                return json.load(f)
        except Exception as config_read_error:
            print(f'Exception has happened while reading config file at==> \t{config_read_error.args}')
            return {}
        except Exception as FileNotFoundError:
            print(f'File not found from project root==>\t{config_path}')
            return {}


class GenericAgent:
    def __init__(self, config):
        self.company_name = input('Enter the company to get financial details through this Agentic Model==>#\t')
        self.custom_prompt = f"Writing report on financial analysis on {self.company_name}"
        # config = ConfigLoader(config_path=config_dir)
        model_selection = input('Select among of pre-defined models from the below '
                                ' list\n Gemini\n Claude\n OpenAI GPT 4O\n').strip().lower()
        if model_selection == 'gemini':
            gemini_api_key = config['gemini_api_key']
            self.model = gemini.Gemini(api_key=gemini_api_key)
        elif model_selection == 'Claude':
            agno_api = config['ANTHROPIC_API_KEY']
            self.model = config['claude_model']['model_id']
        else:
            print(f'Error while model selecting by User')

        self.tool_list = []
        use_yf = input("Enable stock tools? (y/n): ").strip().lower() == 'y'
        if use_yf:
            self.tool_list.append(YFinanceTools(stock_price=True))

        use_reasoning = input("Enable reasoning tools? (y/n): ").strip().lower() == 'y'
        if use_reasoning:
            self.tool_list.append(ReasoningTools)

        # Step 3: Optional settings
        self.markdown = input("Enable markdown output? (y/n): ").strip().lower() == 'y'

    def financial_analyser(self):
        agent = Agent(
            model=self.model,
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
        # Find tip on streaming result is not coming as expectedly.
        # On different segmentation, I'm receiving different result.


        # agent = Agent(
        #     model=self.model,
        #     tools=self.tool_list,
        #     instructions=[
        #             "Use table to display data",
        #             "Respond with only repost, not any other data"
        #         ],
        #     markdown=self.markdown
        # )

        try:
            agent.print_response(message=self.custom_prompt,
                                 stream=True,
                                 show_full_reasoning=True,
                                 stream_intermediate_steps=True
                                 )
        except Exception as agent_error:
            print(f'Getting error while try to fetch target entity as ==>{agent_error.args}')


if __name__ == '__main__':
    config_object = ConfigLoader()
    config = config_object.loading_agent_config(config_dir)
    agent_object = GenericAgent(config)
    agent_object.financial_analyser()

