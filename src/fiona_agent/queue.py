from collections import deque
from dataclasses import dataclass, field
from typing import Deque, Optional

from .agent import Post


@dataclass
class FionaQueue:
    """
    Simple FIFO queue used by Fiona runtime.
    """

    _items: Deque[Post] = field(default_factory=deque)

    def add(self, post: Post) -> None:
        self._items.append(post)

    def pop_next(self) -> Optional[Post]:
        if not self._items:
            return None
        return self._items.popleft()

    def size(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return len(self._items) == 0
