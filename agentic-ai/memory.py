import json
import os

MEMORY_FILE = "agent_memory.json"


class AgentMemory:
    def __init__(self):
        self.logs = []
        self._load()

    def _load(self):
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "r") as f:
                self.logs = json.load(f)

    def log(self, category, content):
        entry = {"type": category, "content": content}
        # self.logs.append({"type": category, "content": content})
        self.logs.append(entry)
        self._save()

    def _save(self):
        with open(MEMORY_FILE, "w") as f:
            json.dump(self.logs, f, indent=2)

    def show_logs(self):
        return self.logs

