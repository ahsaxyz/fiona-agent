from dataclasses import dataclas
from typing import List

from .agent import FionaAgent, Post
from .queue import FionaQueue
from .types import Decision


@dataclass
class ScheduledResult:
    post: Post
    action: str
    score: float
    reason: str


class FionaScheduler:
    """
    Executes batches of posts from the queue using the FionaAgent.
    """

    def __init__(self, agent: FionaAgent, queue: FionaQueue):
        self.agent = agent
        self.queue = queue

    def run_cycle(self, max_items: int = 5) -> List[ScheduledResult]:
        results: List[ScheduledResult] = []

        for _ in range(max_items):
            post = self.queue.pop_next()

            if post is None:
                break

            decision: Decision = self.agent.decide(post)
            self.agent.record(post, decision)

            results.append(
                ScheduledResult(
                    post=post,
                    action=decision.action,
                    score=decision.score,
                    reason=decision.reason,
                )
            )

        return results
