from fiona_agent.agent import Decision, Post
from fiona_agent.feedback import FionaFeedback


def test_feedback_analysis():
    feedback = FionaFeedback()

    post = Post(text="AI agent research architecture")
    decision = Decision(action="reply", score=0.8, reason="test")

    result = feedback.analyze(post, decision)

    assert result.adjustment >= 0
