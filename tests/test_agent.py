from fiona_agent.agent import FionaAgent, Post
from fiona_agent.config import FionaConfig
from fiona_agent.memory import FionaMemory


def test_decide_action():
    cfg = FionaConfig()
    memory = FionaMemory(path="test_memory.json")

    agent = FionaAgent(cfg=cfg, memory=memory)

    post = Post(text="AI agent research architecture")

    decision = agent.decide(post)

    assert decision.action in ["reply", "observe", "ignore"]
