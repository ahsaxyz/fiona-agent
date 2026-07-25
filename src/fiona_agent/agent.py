from dataclasses import dataclass

from .config import FionaConfig
from .memory import FionaMemory
from .policy import FionaPolicy, PolicyThresholds
from .scoring import score_post
from .types import Decision


@dataclass
class Post:
    text: str
    author_handle: str | None = None
    in_reply_to_principal: bool = False


class FionaAgent:
    def __init__(self, cfg: FionaConfig, memory: FionaMemory):
        self.cfg = cfg
        self.memory = memory
        self.policy = FionaPolicy(
            PolicyThresholds(
                reply_threshold=cfg.reply_threshold,
                observe_threshold=cfg.observe_threshold,
            )
        )

    def decide(self, post: Post) -> Decision:
        score, reason = score_post(post)
        return self.policy.choose_action(score, reason)

    def record(self, post: Post, decision: Decision):
        self.memory.store({
            "text": post.text,
            "author": post.author_handle,
            "decision": decision.action,
            "score": decision.score,
        })
