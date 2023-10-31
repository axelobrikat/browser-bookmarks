
from pytest_mock import MockerFixture
from unittest.mock import MagicMock
import pytest
from pathlib import Path

from src.orchestrate import Orchestrator
from src.modes.show_mode import ShowMode
from src.modes.backup_mode import BackupMode
from src.modes.overwrite_mode import OverwriteMode
from src.cli_args import Args
from src.etc.exceptions import Exc


@pytest.fixture
def mock_show_mode(mocker: MockerFixture) -> MagicMock:
    """mock function process_bookmarks from class ShowMode
    """
    return mocker.patch.object(
        ShowMode,
        "process_bookmarks",
    )

@pytest.fixture
def mock_backup_mode(mocker: MockerFixture) -> MagicMock:
    """mock function process_bookmarks from class BackupMode
    """
    return mocker.patch.object(
        BackupMode,
        "process_bookmarks",
    )

@pytest.fixture
def mock_overwrite_mode(mocker: MockerFixture) -> MagicMock:
    """mock function process_bookmarks from class OverwriteMode
    """
    return mocker.patch.object(
        OverwriteMode,
        "process_bookmarks",
    )

@pytest.fixture
def mock_exit(mocker: MockerFixture) -> MagicMock:
    return mocker.patch.object(
        Exc,
        "exit",
    )

@pytest.fixture(autouse=True)
def reset_args():
    """setup function to reset args to default values
    """
    Args.show: bool = False
    Args.backup: bool = False
    Args.overwrite: Path = None


def test_orchestrate_modes_show(mock_show_mode: MagicMock):
    Args.show = True
    Orchestrator.orchestrate_modes()
    mock_show_mode.assert_called_once()

def test_orchestrate_modes_backup(mock_backup_mode: MagicMock):
    Args.backup = True
    Orchestrator.orchestrate_modes()
    mock_backup_mode.assert_called_once()

def test_orchestrate_modes_overwrite(mock_overwrite_mode: MagicMock):
    Args.overwrite = Path("/dummy/path")
    Orchestrator.orchestrate_modes()
    mock_overwrite_mode.assert_called_once()

def test_orchestrate_modes_exit(mock_exit: MagicMock):
    Orchestrator.orchestrate_modes()
    mock_exit.assert_called_once_with(
        f"No action has been specified on CLI as input argument."
    )