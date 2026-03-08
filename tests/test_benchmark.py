from fiona_agent.benchmark import FionaBenchmark


def test_benchmark_runs():
    benchmark = FionaBenchmark(memory_path="tests/test_benchmark_memory.json")
    report = benchmark.run("datasets/sample_posts.json")

    assert report["total_posts"] > 0
    assert "decision_counts" in report
    assert "results" in report
    assert isinstance(report["results"], list)
