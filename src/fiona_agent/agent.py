from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional

from .config import FionaConfig
from .memory import FionaMemory
from .scoring import score_post


Action = Literal["reply", "observe", "ignore"]


@dataclass(frozen=True)
class Post:
    text: str
    author_handle: str | None = None
    in_reply_to_principal: bool = False


@dataclass
class Decision:
    action: Action
    score: float
    reason: str


class FionaAgent:
    def __init__(self, config: Optional[FionaConfig] = None, memory: Optional[FionaMemory] = None):
        self.config = config or FionaConfig()
        self.memory = memory or FionaMemory()

    def decide(self, post: Post) -> Decision:
        breakdown = score_post(post.text, seen_hashes=self.memory.seen_hashes)
        total = breakdown.total

        # Enforce constraint: only reply to principal (or principal-related thread)
        if self.config.allow_reply_to_principal_only:
            if not (post.in_reply_to_principal or post.author_handle == self.config.principal_handle):
                # She may still "observe" high-signal posts; she just won't reply
                if total >= self.config.observe_threshold:
                    return Decision("observe", total, "High-signal post, but reply constrained to principal.")
                return Decision("ignore", total, "Not relevant enough and reply constrained to principal.")

        if total >= self.config.reply_threshold:
            return Decision("reply", total, "Meets reply threshold.")
        if total >= self.config.observe_threshold:
            return Decision("observe", total, "Meets observe threshold.")
        return Decision("ignore", total, "Below thresholds.")

    def record(self, post: Post, decision: Decision) -> None:
        self.memory.add_seen(post.text)
        self.memory.log(
            {
                "text": post.text[:280],
                "author": post.author_handle,
                "in_reply_to_principal": post.in_reply_to_principal,
                "action": decision.action,
                "score": round(decision.score, 3),
                "reason": decision.reason,
            }
        )
        self.memory.save(self.config.memory_path)
