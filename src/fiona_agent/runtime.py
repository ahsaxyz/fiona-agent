from dataclasses import dataclass
from typing import List

from .agent import FionaAgent, Post
from .environment import TimelineEnvironment
from .queue import FionaQueue
from .scheduler import FionaScheduler, ScheduledResult


@dataclass
class RuntimeReport:
    queued_posts: int
    processed_posts: int
    actions: List[str]


class FionaRuntime:
    """
    Coordinates Fiona's full runtime loop.

    Environment -> Queue -> Scheduler -> Agent
    """

    def __init__(self, agent: FionaAgent):
        self.agent = agent
        self.environment = TimelineEnvironment()
        self.queue = FionaQueue()
        self.scheduler = FionaScheduler(agent=self.agent, queue=self.queue)

    def ingest(self, posts: list[Post]) -> None:
        self.environment.load_posts(posts)
        for post in self.environment.stream():
            self.queue.add(post)

    def run_once(self, max_items: int = 5) -> RuntimeReport:
        queued_before = self.queue.size()
        results: list[ScheduledResult] = self.scheduler.run_cycle(max_items=max_items)

        return RuntimeReport(
            queued_posts=queued_before,
            processed_posts=len(results),
            actions=[r.action for r in results],
        )
