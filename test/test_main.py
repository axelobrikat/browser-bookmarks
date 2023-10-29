from pytest_mock import MockerFixture
from unittest.mock import MagicMock
import sys
import pytest

from main import main
from src.cli_args import Args
from src.etc.exceptions import Exc



class TestMainScript():
    """test main.py
    """
    __doc__ = main.__doc__
    
    @pytest.fixture(autouse=True)
    def init(self, mocker: MockerFixture) -> None:
        self.set_cli_args: MagicMock = mocker.patch.object(
            Args,
            "set_cli_args",
        )
        self.check_cli_args: MagicMock = mocker.patch.object(
            Args,
            "check_cli_args",
        )
        self.exit: MagicMock = mocker.patch.object(
            Exc,
            "exit",
        )

    def reset_mocks(self):
        """reset mocked variables
        """
        for mock in [
            self.set_cli_args,
            self.check_cli_args,
            self.exit,
        ]:
            mock.reset_mock()

    def test_main_valid_docopt(self):

        # test case 1: cli input = "-s" #
        sys.argv = r'.\src\main.py -s'.split(' ')
        self.check_cli_args.return_value = ""
        exp_args: dict[str, bool|None] = {
            '-s': True,
            '-b': False,
            '-o': None,
        }
        main()
        self.set_cli_args.assert_called_once_with(exp_args)
        self.check_cli_args.assert_called_once()
        self.exit.assert_not_called()

        # test case 2: cli input = "-b" #
        self.reset_mocks()
        sys.argv = r'.\src\main.py -b'.split(' ')
        self.check_cli_args.return_value = ""
        exp_args: dict[str, bool|None] = {
            '-s': False,
            '-b': True,
            '-o': None,
        }
        main()
        self.set_cli_args.assert_called_once_with(exp_args)
        self.check_cli_args.assert_called_once()
        self.exit.assert_not_called()

        # test case 3: cli input = "-s /correct/dummy/path" #
        self.reset_mocks()
        sys.argv = r'.\src\main.py -o /correct/dummy/path'.split(' ')
        self.check_cli_args.return_value = ""
        exp_args: dict[str, bool|None] = {
            '-s': False,
            '-b': False,
            '-o': '/correct/dummy/path',
        }
        main()
        self.set_cli_args.assert_called_once_with(exp_args)
        self.check_cli_args.assert_called_once()
        self.exit.assert_not_called()

        # test case 4: cli input = "-s /incorrect/dummy/path" #
        self.reset_mocks()
        sys.argv = r'.\src\main.py -o /incorrect/dummy/path'.split(' ')
        self.check_cli_args.return_value = "error message"
        exp_args: dict[str, bool|None] = {
            '-s': False,
            '-b': False,
            '-o': '/incorrect/dummy/path',
        }
        main()
        self.set_cli_args.assert_called_once_with(exp_args)
        self.check_cli_args.assert_called_once()
        self.exit.assert_called_once_with("error message")



# def test_funcc(capsys: CaptureFixture):
#     func()
#     assert capsys.readouterr().out == (
#         "hello world\n"
#         "hello world2\n"
#         "hello world3\n"
#     )
#     print("==> Function for testing captured output is successful.")