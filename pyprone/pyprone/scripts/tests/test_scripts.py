from scripts import __version__
from scripts.getter import get_from


def test_version():
    assert __version__ == '0.1.0'


def test_unknown_source(runner):
    res = runner.invoke(get_from, ["fake_source"])
    assert isinstance(res.exception, NotImplementedError)
    assert res.exit_code == -1


def test_fb_access_missing(env_override, runner):
    env_override("FB_ACCESS_TOKEN", None)
    res = runner.invoke(get_from, ["facebook"])
    assert isinstance(res.exception, EnvironmentError)
    assert res.exit_code == -1


# MOCK it
def test_fb_access_invalid():
    pass


def test_fb_down():
    pass