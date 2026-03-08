from dataclasses import dataclass

from .agent import Decision, Post


@dataclass
class EvaluationResult:
    decision_quality: float
    explanation: str


class FionaEvaluator:
    """
    Lightweight evaluator for Fiona's decisions.

    This module scores whether a reply / observe / ignore decision
    appears reasonable given the post content.
    """

    def evaluate(self, post: Post, decision: Decision) -> EvaluationResult:
        text = post.text.lower()

        high_signal_terms = [
            "ai", "agent", "architecture", "systems",
            "research", "security", "protocol", "design"
        ]

        low_signal_terms = [
            "gm", "wagmi", "pump", "airdrop", "giveaway", "ratio"
        ]

        high_hits = sum(1 for term in high_signal_terms if term in text)
        low_hits = sum(1 for term in low_signal_terms if term in text)

        if decision.action == "reply":
            if high_hits > low_hits:
                return EvaluationResult(
                    decision_quality=1.0,
                    explanation="Reply decision aligned with high-signal content."
                )
            return EvaluationResult(
                decision_quality=0.4,
                explanation="Reply may have been too aggressive for low-signal content."
            )

        if decision.action == "observe":
            return EvaluationResult(
                decision_quality=0.8,
                explanation="Observation is a safe intermediate action."
            )

        return EvaluationResult(
            decision_quality=0.9 if low_hits >= high_hits else 0.5,
            explanation="Ignore decision favored filtering over engagement."
        )
