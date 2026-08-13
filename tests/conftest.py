import pytest


@pytest.fixture(autouse=True)
def disable_heavy_local_models(monkeypatch):
    from src import reranking

    monkeypatch.setattr(reranking.settings, "enable_local_reranker", False)
    reranking._cross_encoder.cache_clear()
