from .scoring import score_post

def decide_action(text: str, threshold_reply: float = 0.6, threshold_observe: float = 0.3) -> str:
    s = score_post(text)
    if s >= threshold_reply:
        return "reply"
    if s >= threshold_observe:
        return "observe"
    return "ignore"
