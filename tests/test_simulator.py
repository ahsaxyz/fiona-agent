from fiona_agent.agent import Post
from fiona_agent.simulator import FionaSimulator


def test_simulator_runs():
    simulator = FionaSimulator(memory_path="tests/test_sim_memory.json")

    posts = [
        Post(text="AI agent architecture research"),
        Post(text="gm wagmi airdrop"),
    ]

    results = simulator.run(posts)

    assert len(results) == 2
    assert "decision" in results[0]
    assert "evaluation" in results[0]
