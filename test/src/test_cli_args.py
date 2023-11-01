import pytest
from pytest_mock import MockerFixture
from pathlib import Path
import os
import psutil
from unittest.mock import MagicMock, patch

from src.cli_args import Args


@pytest.fixture
def mock_overwrite_path_exists(mocker: MockerFixture):
    """mock function overwrite_path_exists

    Args:
        mocker (MockerFixture): pytest MockerFixture

    Returns:
        MagicMock: mocked function
    """
    return mocker.patch.object(
        Args,
        "overwrite_path_exists",
        return_value=True,
    )

@pytest.fixture
def mock_chrome_is_running(mocker: MockerFixture):
    """mock function chrome_is_running

    Args:
        mocker (MockerFixture): pytest MockerFixture

    Returns:
        MagicMock: mocked function
    """
    return mocker.patch.object(
        Args,
        "chrome_is_running",
        return_value=False,
    )

@pytest.fixture
def mock_process_iter(mocker: MockerFixture):
    """mock function psutil.process_iter

    Args:
        mocker (MockerFixture): pytest MockerFixture

    Returns:
        MagicMock: mocked function psutil.process_iter
    """
    return mocker.patch.object(
        psutil,
        "process_iter",
    )


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
    """test setting of CLI input args -o dummy
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

def test_check_cli_args_overwrite_path_exists(
        mock_overwrite_path_exists: MagicMock,
        mock_chrome_is_running: MagicMock
    ):
    """test checking of cli arg -> overwrite_path_exists

    Args:
        mock_overwrite_path_exists (MagicMock): mocked function
        mock_chrome_is_running (MagicMock): mocked function
    """
    # test case 1: overwrite_path_exists mocked to return True (default) #
    err_msg: str = Args.check_cli_args()
    assert err_msg == '', (
        f"Expected no error message, but got {err_msg}"
    )
    mock_overwrite_path_exists.assert_called_once()

    # test case 2: overwrite_path_exists mocked to return False #
    mock_overwrite_path_exists.reset_mock()
    mock_overwrite_path_exists.return_value = False
    Args.overwrite = "/dummy/path"
    err_msg: str = Args.check_cli_args()
    exp_err_msg: str = f"Cannot find specified path '{Args.overwrite}'."
    assert err_msg == exp_err_msg, (
        f'Expected error message "{exp_err_msg}", but got "{err_msg}"'
    )
    mock_overwrite_path_exists.assert_called_once()

def test_check_cli_args_chrome_is_running(
        mock_overwrite_path_exists: MagicMock,
        mock_chrome_is_running: MagicMock
    ):
    """test checking of cli arg -> chrome_is_running

    Args:
        mock_overwrite_path_exists (MagicMock): mocked function
        mock_chrome_is_running (MagicMock): mocked function
    """
    # test case 1: chrome_is_running mocked to return False (default) #
    # a/b) Args.overwrite False and True #
    for Args.overwrite in [True, False]:
        err_msg: str = Args.check_cli_args()
        assert err_msg == '', (
            f"Expected no error message, but got {err_msg}"
        )
        mock_chrome_is_running.assert_called_once()
        mock_chrome_is_running.reset_mock()

    # test case 2: chrome_is_running mocked to return True #
    # a) Args.overwrite False #
    Args.overwrite = False
    mock_chrome_is_running.return_value = True
    err_msg: str = Args.check_cli_args()
    assert err_msg == '', (
        f"Expected no error message, but got {err_msg}"
    )
    mock_chrome_is_running.assert_called_once()
    mock_chrome_is_running.reset_mock()

    # b) Args.overwrite True #
    Args.overwrite = True
    mock_chrome_is_running.return_value = True
    err_msg: str = Args.check_cli_args()
    exp_err_msg: str = f"Chrome is currently running. Make sure Chrome has been terminated."
    assert err_msg == exp_err_msg, (
        f'Expected error message "{exp_err_msg}", but got "{err_msg}"'
    )
    mock_chrome_is_running.assert_called_once()
    
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

def test_chrome_is_running(mock_process_iter: MagicMock):
    """test checking that chrome_is_running
    """
    proc = psutil.Process()
    mock_process_iter.side_effect = lambda arg: {
        proc
    }
    assert Args.chrome_is_running() == False
    print(type(proc))
    print(proc)

def test_test():
    Args.chrome_is_running()

