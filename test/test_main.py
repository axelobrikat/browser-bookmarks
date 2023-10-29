import docopt
import sys
import pytest
from pytest_mock import MockerFixture
from unittest.mock import MagicMock

from main import main
from src.cli_args import Args
from src.etc.exceptions import Exc
from src.orchestrate import Orchestrator


__doc__ = main.__doc__


class TestMainValidDocopt():
    """test main.py with valid cli input args
    """    
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
        self.orchestrate_modes: MagicMock = mocker.patch.object(
            Orchestrator,
            "orchestrate_modes",
        )
        self.exp_args: dict[str, bool|None] = {
            '-s': False,
            '-b': False,
            '-o': None,            
        }

    def reset_mocks(self):
        """reset mocked variables
        """
        for mock in [
            self.set_cli_args,
            self.check_cli_args,
            self.exit,
        ]:
            mock.reset_mock()

    def main_test_cases_valid_docopt(
            self,
            sys_argv: str,
            return_val: str|bool = "",
            exit_called: bool = False,
        ):
        """test cases for testing main() with valid docopt cli args

        Args:
            sys_argv (str): sys.argv cli input args
            return_val (str | bool, optional): return value of mocked func Args.check_cli_args. Defaults to "".
            exit_called (bool, optional): should have function Exc.exit() been called. Defaults to False.
        """
        # arrange #
        sys.argv = sys_argv.split(' ')
        self.check_cli_args.return_value = return_val

        # act #
        main()

        # arrange #
        self.set_cli_args.assert_called_once_with(self.exp_args)
        self.check_cli_args.assert_called_once()
        if exit_called:
            self.exit.assert_called()
        else:
            self.exit.assert_not_called()
            self.orchestrate_modes.assert_called_once()

        # tearDown #
        sys.argv = r'.\src\main.py'
        self.reset_mocks()

    def test_main_valid_docopt_s(self):
        """test main with cli input = "-s"
        """
        self.exp_args = {
            '-s': True,
            '-b': False,
            '-o': None,
        }
        self.main_test_cases_valid_docopt(r'.\src\main.py -s')

    def test_main_valid_docopt_b(self):
        """test main with cli input = "-b"
        """                
        # test case 2: cli input = "-b" #
        self.exp_args: dict[str, bool|None] = {
            '-s': False,
            '-b': True,
            '-o': None,
        }
        self.main_test_cases_valid_docopt(r'.\src\main.py -b')

    def test_main_valid_docopt_o_correct(self):
        """test main with cli input = "-o /correct/dummy/path"
        """
        self.exp_args: dict[str, bool|None] = {
            '-s': False,
            '-b': False,
            '-o': '/correct/dummy/path',
        }
        self.main_test_cases_valid_docopt(r'.\src\main.py -o /correct/dummy/path')

    def test_main_valid_docopt_o_incorrect(self):
        """test main with cli input = "-s /incorrect/dummy/path"
        """
        self.exp_args: dict[str, bool|None] = {
            '-s': False,
            '-b': False,
            '-o': '/incorrect/dummy/path',
        }
        self.main_test_cases_valid_docopt(r'.\src\main.py -o /incorrect/dummy/path', "error_message", True)


class TestMainInvalidDocopt():
    """test main.py with invalid cli input args
    """
    def test_main_invalid_docopt(self):
        """test that docopt raises an error when cli input is incorrect
        """
        for argv in [
            r'.\src\main.py',
            r'.\src\main.py -o',
            # r'.\src\main.py -o ', # not testable with .split(" ")
            # r'.\src\main.py -o ""', # not testable with .split(" ")
            r'.\src\main.py -b /dummy/path',
            r'.\src\main.py -s /dummy/path',
            r'.\src\main.py -a',
            r'.\src\main.py -v',
        ]:
            sys.argv = argv.split(' ')
            with pytest.raises(docopt.DocoptExit):
                main()


# def test_funcc(capsys: CaptureFixture):
#     func()
#     assert capsys.readouterr().out == (
#         "hello world\n"
#         "hello world2\n"
#         "hello world3\n"
#     )
#     print("==> Function for testing captured output is successful.")