from unittest.mock import Mock, patch

from src.etc.exceptions import Exc

def test_format_exc_msg():
    """test formatting of exception message
    """
    msg: str = "dummy message"
    assert Exc.format_exc_msg(msg) == (
            f"\n============"
            f"\nError occured, Program end"
            f"\n============"
            f"\ndummy message"
            f"\n============\n"
    )

@patch("sys.exit")
@patch("src.etc.exceptions.Exc.format_exc_msg")
def test_exit(format_exc_msg: Mock, exit: Mock):
    """test exiting program when error occurs and printing information

    Args:
        format_exc_msg (Mock): mock exception message
        exit (Mock): mock sys.exit built-in func
    """    
    format_exc_msg.return_value = "dummy"
    Exc.exit("dummy")
    exit.assert_called_once_with("dummy")