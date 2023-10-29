
from pytest_mock import MockerFixture
from unittest.mock import MagicMock
import pytest
from pathlib import Path

from src.orchestrate import Orchestrator
from src.bib import Bib
from src.cli_args import Args
from src.etc.exceptions import Exc


@pytest.fixture
def mock_show_bookmarks(mocker: MockerFixture) -> MagicMock:
    return mocker.patch.object(
        Bib,
        "show_bookmarks",
    )

@pytest.fixture
def mock_backup_bookmarks(mocker: MockerFixture) -> MagicMock:
    return mocker.patch.object(
        Bib,
        "backup_bookmarks",
    )

@pytest.fixture
def mock_overwrite_bookmarks(mocker: MockerFixture) -> MagicMock:
    return mocker.patch.object(
        Bib,
        "overwrite_bookmarks",
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


def test_orchestrate_modes_show(mock_show_bookmarks: MagicMock):
    Args.show = True
    Orchestrator.orchestrate_modes()
    mock_show_bookmarks.assert_called_once()

def test_orchestrate_modes_backup(mock_backup_bookmarks: MagicMock):
    Args.backup = True
    Orchestrator.orchestrate_modes()
    mock_backup_bookmarks.assert_called_once()

def test_orchestrate_modes_overwrite(mock_overwrite_bookmarks: MagicMock):
    Args.overwrite = Path("/dummy/path")
    Orchestrator.orchestrate_modes()
    mock_overwrite_bookmarks.assert_called_once()

def test_orchestrate_modes_exit(mock_exit: MagicMock):
    Orchestrator.orchestrate_modes()
    mock_exit.assert_called_once_with(
        f"No action has been specified on CLI as input argument."
    )