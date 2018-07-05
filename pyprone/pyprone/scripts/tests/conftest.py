"""
Just a conftest for scripts
"""

import os
import pytest
from click.testing import CliRunner


@pytest.fixture(scope="function")
def runner():
    return CliRunner()


@pytest.fixture(scope="function")
def env_override():
    orig = None
    out_key = None
    def return_func(key, value):
        orig = os.environ.get(key)
        out_key = key
        os.environ[key] = value

    yield return_func
    if orig:
        os.environ[out_key] = orig