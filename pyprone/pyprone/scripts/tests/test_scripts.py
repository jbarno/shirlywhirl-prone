import pytest
from scripts import __version__
from scripts.getter import get_from


def test_version():
    assert __version__ == '0.1.0'


def test_unknown_source(runner):
    with pytest.raises(NotImplemented):
        runner.invoke(get_from, ["fake_source"])


def test_fb_access_missing(env_override, runner):
    env_override("FB_ACCESS_TOKEN", None)
    with pytest.raises(EnvironmentError):
        res = runner.invoke(get_from, ["facebook"])


# MOCK it
def test_fb_access_invalid():
    with pytest.raises(BaseException):
        pass


def test_fb_down():
    pass