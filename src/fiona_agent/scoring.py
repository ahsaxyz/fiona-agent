from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class ScoreBreakdown:
    relevance: float
    novelty: float
    quality: float

    @property
    def total(self) -> float:
        # simple weighted sum; tweak later
        return min(1.0, 0.45 * self.relevance + 0.25 * self.novelty + 0.30 * self.quality)


HIGH_SIGNAL_KEYWORDS = (
    "agent", "ai", "architecture", "systems", "security", "research",
    "openclaw", "solana", "protocol", "design", "implementation",
)

LOW_SIGNAL_KEYWORDS = (
    "ratio", "gm", "wagmi", "airdrop", "pump", "free money", "dm me",
    "giveaway", "memecoin", "onlyfans",
)


def _keyword_hits(text: str, keywords: Iterable[str]) -> int:
    t = text.lower()
    return sum(1 for k in keywords if k in t)


def score_post(post, *, seen_hashes: set[str] | None = None):
    """
    Very lightweight heuristic scoring.
    Replace later with embeddings/classifiers if you want.
    """

    text = post.text

    if not text:
        return 0.0, "empty"

    hs = _keyword_hits(text, HIGH_SIGNAL_KEYWORDS)
    ls = _keyword_hits(text, LOW_SIGNAL_KEYWORDS)

    relevance = min(1.0, hs * 0.18)
    quality = max(0.0, min(1.0, 0.6 - ls * 0.25 + hs * 0.08))

    novelty = 0.7
    if seen_hashes is not None:
        h = str(hash(text.strip().lower()))
        novelty = 0.2 if h in seen_hashes else 0.7

    breakdown = ScoreBreakdown(
        relevance=relevance,
        novelty=novelty,
        quality=quality,
    )

    reason = f"relevance={breakdown.relevance:.2f}, novelty={breakdown.novelty:.2f}, quality={breakdown.quality:.2f}"

    return breakdown.total, reason
