from fiona_agent.scoring import score_post
from fiona_agent.agent import Post


def test_score_post_high_signal():
    post = Post(text="AI agent architecture and systems design")

    score, reason = score_post(post)

    assert score > 0
