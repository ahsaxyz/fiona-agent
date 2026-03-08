from dataclasses import dataclass


@dataclass(frozen=True)
class SignalResult:
    name: str
    score: float
    reason: str


HIGH_SIGNAL_KEYWORDS = (
    "agent",
    "ai",
    "architecture",
    "systems",
    "security",
    "research",
    "openclaw",
    "solana",
    "protocol",
    "design",
    "implementation",
)

LOW_SIGNAL_KEYWORDS = (
    "ratio",
    "gm",
    "wagmi",
    "airdrop",
    "pump",
    "free money",
    "dm me",
    "giveaway",
    "memecoin",
    "onlyfans",
)


def keyword_signal(text: str) -> SignalResult:
    lowered = text.lower()

    high_hits = sum(1 for kw in HIGH_SIGNAL_KEYWORDS if kw in lowered)
    low_hits = sum(1 for kw in LOW_SIGNAL_KEYWORDS if kw in lowered)

    raw_score = 0.15 * high_hits - 0.2 * low_hits
    score = max(0.0, min(1.0, 0.5 + raw_score))

    return SignalResult(
        name="keyword_signal",
        score=score,
        reason=f"high_hits={high_hits}, low_hits={low_hits}",
    )


def length_signal(text: str) -> SignalResult:
    length = len(text.strip())

    if length == 0:
        score = 0.0
        reason = "empty text"
    elif length < 20:
        score = 0.3
        reason = "very short post"
    elif length < 80:
        score = 0.6
        reason = "moderate length"
    else:
        score = 0.8
        reason = "substantial length"

    return SignalResult(
        name="length_signal",
        score=score,
        reason=reason,
    )


def punctuation_signal(text: str) -> SignalResult:
    exclamations = text.count("!")
    questions = text.count("?")

    if exclamations >= 3:
        score = 0.25
        reason = "overuse of exclamation marks"
    elif questions >= 2:
        score = 0.5
        reason = "question-heavy post"
    else:
        score = 0.75
        reason = "normal punctuation profile"

    return SignalResult(
        name="punctuation_signal",
        score=score,
        reason=reason,
    )
