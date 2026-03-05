import random

class FionaAgent:

    def __init__(self):
        self.interest_threshold = 0.6

    def evaluate_post(self, post):
        """
        Simulates Fiona evaluating the signal quality of a post.
        """

        keywords = [
            "AI",
            "agent",
            "research",
            "architecture",
            "systems",
            "learning"
        ]

        score = 0

        for word in keywords:
            if word.lower() in post.lower():
                score += 0.2

        return min(score, 1.0)

    def decide_action(self, post):
        score = self.evaluate_post(post)

        if score >= self.interest_threshold:
            return "reply"
        elif score > 0.2:
            return "observe"
        else:
            return "ignore"


if __name__ == "__main__":

    fiona = FionaAgent()

    test_post = "New AI agent architecture released today"

    action = fiona.decide_action(test_post)

    print(f"Fiona decision: {action}")
