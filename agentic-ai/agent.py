from memory import AgentMemory
from tools import available_tools


class Agent:
    def __init__(self):
        self.memory = AgentMemory()

    def process(self, user_input):
        self.memory.log("input", user_input)

        results = []
        for tool in available_tools:
            if tool.match(user_input):
                result = tool.run(user_input)
                self.memory.log("action", result)
                # return result
                results.append(result)

        if not results:
            return "Sorry, I didn't understand."
        return "\n".join(results)

