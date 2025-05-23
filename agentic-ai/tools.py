import datetime
import importlib
import os


class Tool:
    def __init__(self, name, keywords, action_func):
        self.name = name
        self.keywords = keywords
        self.action_func = action_func

    def match(self, input_text):
        return any(keyword in input_text.lower() for keyword in self.keywords)

    def run(self, input_text):
        return self.action_func(input_text)


# ---- Tool functions ----
def echo_tool(text):
    return f"Echo: {text}"


def time_tool(_):
    now = datetime.datetime.now()
    return f"Current time is {now.strftime('%H:%M:%S')}"


def memory_tool(_):
    from memory import AgentMemory
    mem = AgentMemory()
    return f"Logs: {mem.show_logs()}"


def save_note_tool(text):
    with open("agent_notes.txt", "a") as f:
        f.write(text + "\n")
    return "Note saved."


# ---- List of tools ----
for file in os.listdir("plugins"):
    if file.endswith(".py") and file != "__init__.py":
        mod = importlib.import_module(f"plugins.{file[:-3]}")
        if hasattr(mod, "respond"):
            available_tools = [
                Tool("echo", ["say", "repeat"], echo_tool),
                Tool("time", ["time", "clock"], time_tool),
                Tool("note", ["note", "save", "remember"], save_note_tool),
                Tool("memory", ["history", "memory", "logs"], memory_tool),
            ]

