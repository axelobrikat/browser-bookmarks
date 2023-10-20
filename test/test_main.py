from pytest import CaptureFixture
import sys
from pathlib import Path

from main import main
# from src.main import func

def test_main():
    assert main() == Path("C:\Users\Axel\AppData\Local\Google\Chrome\User Data\Default\Bookmarks")
#     __doc__ = main.__doc__
#     sys.argv = '.\\src\\main.py -v'.split(' ')
#     assert main.main() == {
#         '--quiet': 0,
#         '--verbose': 1,
#     }

# def test_funcc(capsys: CaptureFixture):
#     func()
#     assert capsys.readouterr().out == (
#         "hello world\n"
#         "hello world2\n"
#         "hello world3\n"
#     )
#     print("==> Function for testing captured output is successful.")