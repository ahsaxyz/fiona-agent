from fiona_agent.agent import FionaAgent, Post
from fiona_agent.config import FionaConfig
from fiona_agent.memory import FionaMemory


def test_decide_action():
    agent = FionaAgent(cfg=FionaConfig(), memory=FionaMemory())
    post = Post(text="AI agent research architecture")

    decision = agent.decide(post)

    assert decision.action in ["reply", "observe", "ignore"]
