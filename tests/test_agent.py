from fiona_agent.agent import FionaAgent

def test_decide_action():
    agent = FionaAgent(cfg={}, memory={})
    decision = agent.decide("AI agent research architecture")
    assert decision in ["reply", "observe", "ignore"]
