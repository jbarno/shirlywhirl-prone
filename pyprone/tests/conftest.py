"""
Just a conftest for scripts
"""

import os
import pytest
from click.testing import CliRunner


@pytest.fixture(scope="function")
def runner():
    return CliRunner()
