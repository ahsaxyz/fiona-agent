from dataclasses import dataclass

@dataclass(frozen=True)
class FionaConfig:
    # Thresholds for decisions
    reply_threshold: float = 0.65
    observe_threshold: float = 0.35

    # Behavioral constraints (documented + enforceable)
    allow_reply_to_principal_only: bool = True
    principal_handle: str = "@ahsaxyz"

    # Memory
    memory_path: str = "data/memory.json"
