from fiona_agent.agent import FionaAgent

def test_decide_action():
    agent = FionaAgent(cfg={}, memory={})
    action = agent.decide_action("AI agent research architecture")
    assert action in ["reply", "observe", "ignore"]
