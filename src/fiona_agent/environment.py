from dataclasses import dataclass, field
from typing import List

from .agent import Post


@dataclass
class TimelineEnvironment:
    """
    Represents Fiona's observable environment.

    This models a simplified timeline containing posts Fiona
    can evaluate and decide whether to engage with.
    """

    posts: List[Post] = field(default_factory=list)

    def add_post(self, post: Post):
        self.posts.append(post)

    def load_posts(self, posts: List[Post]):
        self.posts.extend(posts)

    def stream(self):
        """
        Generator that yields posts sequentially.
        Useful for simulation loops.
        """
        for post in self.posts:
            yield post
