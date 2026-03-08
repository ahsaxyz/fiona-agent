from fiona_agent.agent import FionaAgent, Post
from fiona_agent.config import FionaConfig
from fiona_agent.memory import FionaMemory

agent = FionaAgent(
    cfg=FionaConfig(),
    memory=FionaMemory("memory.json")
)

posts = [
    Post(text="AI architecture research"),
    Post(text="gm wagmi pump"),
    Post(text="protocol design for distributed systems")
]

for p in posts:
    decision = agent.decide(p)
    print(p.text, "→", decision)
