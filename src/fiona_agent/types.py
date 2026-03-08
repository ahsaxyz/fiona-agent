from dataclasses import dataclass


@dataclass
class Decision:
    action: str
    score: float
    reason: str
