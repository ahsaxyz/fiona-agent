def score_post(text: str) -> float:
    """
    Very simple scoring model (placeholder).
    Replace with embeddings / classifiers later.
    """
    keywords = ["agent", "ai", "systems", "architecture", "security", "build"]
    hits = sum(1 for k in keywords if k in text.lower())
    return min(1.0, hits * 0.2)
