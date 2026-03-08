from dataclasses import asdict
from typing import Iterable

from .agent import FionaAgent, Post
from .config import FionaConfig
from .evaluator import FionaEvaluator
from .memory import FionaMemory


class FionaSimulator:
    """
    Runs Fiona against a batch of posts and evaluates the outcomes.
    Useful for local experiments, quick benchmarks, and future tuning.
    """

    def __init__(self, memory_path: str = "data/sim_memory.json"):
        self.cfg = FionaConfig()
        self.memory = FionaMemory(memory_path)
        self.agent = FionaAgent(cfg=self.cfg, memory=self.memory)
        self.evaluator = FionaEvaluator()

    def run(self, posts: Iterable[Post]) -> list[dict]:
        results = []

        for post in posts:
            decision = self.agent.decide(post)
            evaluation = self.evaluator.evaluate(post, decision)

            results.append(
                {
                    "post": post.text,
                    "author": post.author_handle,
                    "in_reply_to_principal": post.in_reply_to_principal,
                    "decision": asdict(decision),
                    "evaluation": asdict(evaluation),
                }
            )

        return results


def demo():
    simulator = FionaSimulator()

    posts = [
        Post(text="New AI agent architecture research released today"),
        Post(text="gm wagmi free airdrop pump"),
        Post(text="Protocol design and systems implementation discussion"),
        Post(text="ratio + giveaway + memecoin launch"),
    ]

    results = simulator.run(posts)

    for item in results:
        print("=" * 60)
        print("POST:", item["post"])
        print("DECISION:", item["decision"])
        print("EVALUATION:", item["evaluation"])


if __name__ == "__main__":
    demo()
