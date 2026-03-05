from dataclasses import dataclass

from .config import FionaConfig
from .memory import FionaMemory
from .scoring import score_post


@dataclass
class Post:
    text: str
    author_handle: str | None = None
    in_reply_to_principal: bool = False


@dataclass
class Decision:
    action: str
    score: float
    reason: str


class FionaAgent:
    def __init__(self, cfg: FionaConfig, memory: FionaMemory):
        self.cfg = cfg
        self.memory = memory

    def decide(self, post: Post) -> Decision:
        score, reason = score_post(post)

        if score >= self.cfg.reply_threshold:
            action = "reply"
        elif score >= self.cfg.observe_threshold:
            action = "observe"
        else:
            action = "ignore"

        return Decision(action=action, score=score, reason=reason)

    def record(self, post: Post, decision: Decision):
        self.memory.store({
            "text": post.text,
            "author": post.author_handle,
            "decision": decision.action,
            "score": decision.score
        })
