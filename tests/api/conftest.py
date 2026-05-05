import pytest

from utils.client import ApiClient


@pytest.fixture(scope="session")
def api():
    return ApiClient()
