from fiona_agent.signals import keyword_signal, length_signal, punctuation_signal


def test_keyword_signal_high_signal():
    result = keyword_signal("AI agent architecture and systems research")
    assert result.score > 0.5


def test_length_signal_empty():
    result = length_signal("")
    assert result.score == 0.0


def test_punctuation_signal_normal():
    result = punctuation_signal("This is a normal post about agent design.")
    assert result.score > 0.5
