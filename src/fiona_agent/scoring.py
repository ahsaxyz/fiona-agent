from __future__ import annotations

from dataclasses import dataclass

from .signals import keyword_signal, length_signal, punctuation_signal


@dataclass(frozen=True)
class ScoreBreakdown:
    relevance: float
    novelty: float
    quality: float

    @property
    def total(self) -> float:
        return min(1.0, 0.45 * self.relevance + 0.25 * self.novelty + 0.30 * self.quality)


def score_post(post, *, seen_hashes: set[str] | None = None):
    text = post.text

    if not text:
        return 0.0, "empty"

    keyword_result = keyword_signal(text)
    length_result = length_signal(text)
    punctuation_result = punctuation_signal(text)

    relevance = keyword_result.score
    quality = (length_result.score + punctuation_result.score) / 2

    novelty = 0.7
    if seen_hashes is not None:
        h = str(hash(text.strip().lower()))
        novelty = 0.2 if h in seen_hashes else 0.7

    breakdown = ScoreBreakdown(
        relevance=relevance,
        novelty=novelty,
        quality=quality,
    )

    reason = (
        f"{keyword_result.reason}; "
        f"{length_result.reason}; "
        f"{punctuation_result.reason}"
    )

    return breakdown.total, reason
