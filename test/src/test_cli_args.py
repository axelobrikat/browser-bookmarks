from pytest_mock import MockerFixture
from pathlib import Path
import os
from unittest.mock import MagicMock

from src.cli_args import Args


def test_set_cli_args_b():
    """test setting of CLI input args -b
    """
    args: dict[str, str] = {
        '-b': True,
        '-o': None,
        '-s': False,
    }
    Args.set_cli_args(args)
    assert Args.show == False
    assert Args.backup == True
    assert Args.overwrite == None

def test_set_cli_args_o():
    """test setting of CLI input args -o
    """
    args: dict[str, str] = {
        '-b': False,
        '-o': 'dummy',
        '-s': False,
    }
    Args.set_cli_args(args)
    assert Args.show == False
    assert Args.backup == False
    assert Args.overwrite == Path('dummy')

def test_set_cli_args_s():
    """test setting of CLI input args -s
    """
    args: dict[str, str] = {
        '-b': False,
        '-o': None,
        '-s': True,
    }
    Args.set_cli_args(args)
    assert Args.show == True
    assert Args.backup == False
    assert Args.overwrite == None

def test_check_cli_args_overwrite_path_exists(mocker: MockerFixture):
    """test checking of cli arg -> overwrite_path_exists

    Args:
        mocker (MockerFixture): MockerFixture
    """
    overwrite_path_exists: MagicMock = mocker.patch.object(
        Args,
        "overwrite_path_exists",
    )

    # test case 1: overwrite_path_exists mocked to return True #
    overwrite_path_exists.return_value = True
    err_msg: str = Args.check_cli_args()
    assert err_msg == '', (
        f"Expected no error message, but got {err_msg}"
    )
    overwrite_path_exists.assert_called_once()

    # test case 2: overwrite_path_exists mocked to return False #
    overwrite_path_exists.reset_mock()
    overwrite_path_exists.return_value = False
    Args.overwrite = "/dummy/path"
    err_msg: str = Args.check_cli_args()
    exp_err_msg: str = f"Cannot find specified path '{Args.overwrite}'."
    assert err_msg == exp_err_msg, (
        f'Expected error message "{exp_err_msg}", but got "{err_msg}"'
    )
    overwrite_path_exists.assert_called_once()
    
def test_overwrite_path_exists():
    """test checking that overwrite_path_exists
    """
    # test case 1: Path not set #
    Args.overwrite = None
    assert Args.overwrite_path_exists() == True
    
    # test case 2: Path does not exist #
    Args.overwrite = Path("not existing path")
    assert Args.overwrite_path_exists() == False
    
    # test case 3: Path does exist #
    Args.overwrite = Path(os.curdir)
    assert Args.overwrite_path_exists() == True