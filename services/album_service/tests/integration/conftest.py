import os
import pytest

@pytest.fixture(scope="session", autouse=True)
def set_env_variables():
    os.environ["DATABASE_URL"] = os.environ.get("DATABASE_URL")
