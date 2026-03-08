from fiona_agent.environment import TimelineEnvironment
from fiona_agent.agent import Post


def test_environment_stream():
    env = TimelineEnvironment()

    env.add_post(Post(text="AI research"))
    env.add_post(Post(text="gm wagmi"))

    posts = list(env.stream())

    assert len(posts) == 2
