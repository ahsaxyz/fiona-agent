from fiona_agent.policy import FionaPolicy, PolicyThresholds


def test_policy_reply():
    policy = FionaPolicy(
        PolicyThresholds(reply_threshold=0.7, observe_threshold=0.4)
    )

    decision = policy.choose_action(0.9, "high signal")
    assert decision.action == "reply"


def test_policy_observe():
    policy = FionaPolicy(
        PolicyThresholds(reply_threshold=0.7, observe_threshold=0.4)
    )

    decision = policy.choose_action(0.5, "medium signal")
    assert decision.action == "observe"


def test_policy_ignore():
    policy = FionaPolicy(
        PolicyThresholds(reply_threshold=0.7, observe_threshold=0.4)
    )

    decision = policy.choose_action(0.2, "low signal")
    assert decision.action == "ignore"
