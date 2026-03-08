from fiona_agent.agent import Post
from fiona_agent.types import Decision
from fiona_agent.evaluator import FionaEvaluator


def test_evaluator_reply_quality():
    evaluator = FionaEvaluator()
    post = Post(text="AI agent architecture research")
    decision = Decision(action="reply", score=0.9, reason="high signal")

    result = evaluator.evaluate(post, decision)

    assert result.decision_quality > 0.5
