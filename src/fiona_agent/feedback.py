from dataclasses import dataclass

from .agent import Decision, Post


@dataclass
class FeedbackResult:
    adjustment: float
    explanation: str


class FionaFeedback:
    """
    Evaluates whether Fiona's decision should strengthen or weaken
    future scoring behavior.
    """

    def analyze(self, post: Post, decision: Decision) -> FeedbackResult:
        text = post.text.lower()

        high_signal = any(
            k in text for k in ["agent", "ai", "architecture", "research", "protocol"]
        )

        low_signal = any(
            k in text for k in ["gm", "wagmi", "airdrop", "giveaway", "pump"]
        )

        if decision.action == "reply" and high_signal:
            return FeedbackResult(
                adjustment=0.1,
                explanation="Reply aligned with high-signal content",
            )

        if decision.action == "reply" and low_signal:
            return FeedbackResult(
                adjustment=-0.15,
                explanation="Reply triggered on low-signal content",
            )

        if decision.action == "ignore" and high_signal:
            return FeedbackResult(
                adjustment=-0.1,
                explanation="Missed high-signal opportunity",
            )

        return FeedbackResult(
            adjustment=0.0,
            explanation="Decision acceptable",
        )
