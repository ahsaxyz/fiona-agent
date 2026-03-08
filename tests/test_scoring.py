from fiona_agent.scoring import score_post

def test_score_post_high_signal():
    text = "AI agent architecture and systems design"
    score = score_post(text)

    assert score.total > 0
