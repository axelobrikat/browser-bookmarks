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