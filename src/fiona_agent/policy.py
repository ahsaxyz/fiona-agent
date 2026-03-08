from dataclasses import dataclass

from .types import Decision


@dataclass
class PolicyThresholds:
    reply_threshold: float
    observe_threshold: float


class FionaPolicy:
    """
    Encapsulates Fiona's action-selection policy.

    Converts a numeric score into a reply / observe / ignore decision.
    """

    def __init__(self, thresholds: PolicyThresholds):
        self.thresholds = thresholds

    def choose_action(self, score: float, reason: str) -> Decision:
        if score >= self.thresholds.reply_threshold:
            action = "reply"
        elif score >= self.thresholds.observe_threshold:
            action = "observe"
        else:
            action = "ignore"

        return Decision(
            action=action,
            score=score,
            reason=reason,
        )
