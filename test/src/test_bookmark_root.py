from pytest import CaptureFixture

from src.bookmark_root import Root


def test_init():
    """test __init__ of Root class
    """
    # test case 1: no "name" in content dict #
    r = Root("test", {"foo": "bar"})
    assert r.root_name == "test"
    assert r.content == {"foo": "bar"}
    assert r.name == ""

    # test case 2: "name" in content dict #
    r = Root("test", {"name": "bar"})
    assert r.root_name == "test"
    assert r.content == {"name": "bar"}
    assert r.name == "bar"

def test_str():
    """test __str__ of Root class
    """
    r = Root("test", {"foo": "bar"})
    assert r.__str__() == "This is bookmark root: test."

def test_output_name(capsys: CaptureFixture):
    """test printing name to cli

    Args:
        capsys (CaptureFixture): captures output to cli
    """
    r = Root("test", {"name": "bar"})
    r.output_name()
    assert capsys.readouterr().out == (
        "bar\n"
    )