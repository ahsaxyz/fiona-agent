from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from .agent import FionaAgent, Post
from .config import FionaConfig
from .memory import FionaMemory


class FionaBenchmark:
    """
    Runs Fiona on a sample dataset and summarizes decision outcomes.
    """

    def __init__(self, memory_path: str = "data/benchmark_memory.json"):
        self.cfg = FionaConfig()
        self.memory = FionaMemory(memory_path)
        self.agent = FionaAgent(cfg=self.cfg, memory=self.memory)

    def load_posts(self, path: str) -> list[Post]:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        return [
            Post(
                text=item["text"],
                author_handle=item.get("author_handle"),
                in_reply_to_principal=item.get("in_reply_to_principal", False),
            )
            for item in data
        ]

    def run(self, dataset_path: str) -> dict:
        posts = self.load_posts(dataset_path)
        counts = Counter()
        scored_results = []

        for post in posts:
            decision = self.agent.decide(post)
            counts[decision.action] += 1

            scored_results.append(
                {
                    "text": post.text,
                    "action": decision.action,
                    "score": decision.score,
                    "reason": decision.reason,
                }
            )

        return {
            "total_posts": len(posts),
            "decision_counts": dict(counts),
            "results": scored_results,
        }


def demo():
    benchmark = FionaBenchmark()
    report = benchmark.run("datasets/sample_posts.json")

    print("Benchmark Summary")
    print("-----------------")
    print("Total posts:", report["total_posts"])
    print("Decision counts:", report["decision_counts"])
    print()

    for row in report["results"]:
        print(f"{row['action']:>7} | {row['score']:.3f} | {row['text']}")


if __name__ == "__main__":
    demo()
