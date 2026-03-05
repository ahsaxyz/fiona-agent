from __future__ import annotations

import argparse

from .agent import FionaAgent, Post
from .config import FionaConfig
from .memory import FionaMemory


def main() -> int:
    parser = argparse.ArgumentParser(prog="fiona-agent", description="Fiona agent prototype CLI")
    parser.add_argument("--text", required=True, help="Post text to evaluate")
    parser.add_argument("--author", default=None, help="Author handle (e.g. @someone)")
    parser.add_argument("--reply-to-principal", action="store_true", help="Mark as in reply to principal thread")
    args = parser.parse_args()

    cfg = FionaConfig()
    mem = FionaMemory.load(cfg.memory_path)
    agent = FionaAgent(cfg, mem)

    post = Post(text=args.text, author_handle=args.author, in_reply_to_principal=args.reply_to_principal)
    decision = agent.decide(post)
    agent.record(post, decision)

    print(f"action={decision.action} score={decision.score:.3f} reason={decision.reason}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
