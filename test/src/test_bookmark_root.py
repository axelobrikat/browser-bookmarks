from src.bookmark_root import Root

def test_str():
    """test __str__ of Root class
    """
    r = Root("test", {"foo": "bar"})
    assert r.__str__() == "This is bookmark root: test."