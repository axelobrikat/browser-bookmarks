from src.etc.exceptions import Exc

def test_format_exc_msg():
    msg: str = "dummy message"
    assert Exc.format_exc_msg(msg) == (
            f"\n============"
            f"\ndummy message"
            f"\n============\n"
    )