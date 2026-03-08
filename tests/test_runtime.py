from fiona_agent.agent import FionaAgent, Post
from fiona_agent.config import FionaConfig
from fiona_agent.memory import FionaMemory
from fiona_agent.runtime import FionaRuntime


def test_runtime_run_once():
    agent = FionaAgent(
        cfg=FionaConfig(),
        memory=FionaMemory("tests/test_runtime_memory.json"),
    )

    runtime = FionaRuntime(agent)

    runtime.ingest([
        Post(text="AI agent architecture research"),
        Post(text="gm wagmi giveaway"),
    ])

    report = runtime.run_once(max_items=2)

    assert report.queued_posts == 2
    assert report.processed_posts == 2
    assert len(report.actions) == 2
