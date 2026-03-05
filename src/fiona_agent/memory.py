import json
from pathlib import Path


class FionaMemory:

    def __init__(self, path: str):
        self.path = Path(path)
        self.data = []

    @classmethod
    def load(cls, path: str):
        mem = cls(path)

        if mem.path.exists():
            mem.data = json.loads(mem.path.read_text())

        return mem

    def store(self, entry):
        self.data.append(entry)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.data, indent=2))
