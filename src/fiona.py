from .scoring import score_pos

class Fiona:

    def __init__(self, threshold_reply: float = 0.6, threshold_observe: float = 0.3):
        self.threshold_reply = threshold_reply
        self.threshold_observe = threshold_observe

    def evaluate(self, text: str) -> float:
        """
        Evaluate a piece of content and return its signal score.
        """
        return score_post(text)

    def decide_action(self, text: str) -> str:
        """
        Decide how Fiona should respond to a piece of content.
        """
        score = self.evaluate(text)

        if score >= self.threshold_reply:
            return "reply"

        if score >= self.threshold_observe:
            return "observe"

        return "ignore"

    def process(self, text: str) -> dict:
        """
        Full processing pipeline for a timeline item.
        """
        score = self.evaluate(text)
        action = self.decide_action(text)

        return {
            "text": text,
            "score": score,
            "action": action
        }
