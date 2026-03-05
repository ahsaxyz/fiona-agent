from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from typing import Any


@dataclass
class FionaMemory:
    seen_hashes: set[str] = field(default_factory=set)
    notes: list[dict[str, Any]] = field(default_factory=list)

    def add_seen(self, text: str) -> None:
        self.seen_hashes.add(str(hash(text.strip().lower())))

    def log(self, entry: dict[str, Any]) -> None:
        self.notes.append(entry)

    def save(self, path: str) -> None:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        payload = {
            "seen_hashes": sorted(self.seen_hashes),
            "notes": self.notes[-500:],  # keep it bounded
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)

    @classmethod
    def load(cls, path: str) -> "FionaMemory":
        if not os.path.exists(path):
            return cls()
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        mem = cls(
            seen_hashes=set(data.get("seen_hashes", [])),
            notes=list(data.get("notes", [])),
        )
        return mem
