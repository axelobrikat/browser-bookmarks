import pytest
from pathlib import Path
from unittest.mock import Mock

from src.cli_args import Args

@pytest.fixture
def mock_check_overwrite_path_exists(mocker):
    mock = Mock()
    with mocker.patch('src.cli_args.Args.check_overwrite_path_exists', return_value=mock):
        yield mock

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

def test_check_cli_args(mock_check_overwrite_path_exists: Mock):
    Args.check_cli_args()
    assert mock_check_overwrite_path_exists.assert_called_once()