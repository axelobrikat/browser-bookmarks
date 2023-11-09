import pytest
import os
from pytest import CaptureFixture
from pytest_mock import MockerFixture
from pathlib import Path
from unittest.mock import MagicMock, patch
from datetime import datetime

from src.modes.backup_mode import BackupMode
from src.modes import backup_mode
from src.etc.paths import ROOT


@pytest.fixture
def mock_copy_bookmarks_file(mocker: MockerFixture) -> MagicMock:
    return mocker.patch.object(
        BackupMode,
        "copy_bookmarks_file",
    )


def test_init():
    """test __init__ of class
    """
    b = BackupMode()
    assert b.dest_path == Path(__file__).resolve().parent.parent.parent.parent / "data"

def test_process_bookmarks(mock_copy_bookmarks_file: MagicMock):
    """test function call

    Args:
        mock_copy_bookmarks_file (MagicMock): mocked function
    """
    b = BackupMode()
    b.process_bookmarks()
    mock_copy_bookmarks_file.assert_called_once()

def test_copy_bookmarks_file_success(capsys: CaptureFixture):
    """test successful copying of bookmarks file and outputtung of success message

    Args:
        capsys (CaptureFixture): capture cli output
    """
    b = BackupMode()
    mock_bookmarks: Path = Path(ROOT, "test", "testdata", "231030_Bookmarks")

    with patch.object(BackupMode, "get_current_datetime", return_value="dummy"):
        with patch.object(backup_mode, "BOOKMARKS", mock_bookmarks):
            b.copy_bookmarks_file()

    test_file: Path = ROOT / "data" / "dummy_Backup_Bookmarks"
    assert test_file.exists() == True
    os.remove(test_file)

    assert capsys.readouterr().out == (
        f"Copy of file {mock_bookmarks} successfully saved"
        f"\n as {test_file}.\n"
    )

def test_copy_bookmarks_file_fail():
    """check that SystemExit Exception gets raised
    """
    b = BackupMode()

    with patch.object(backup_mode, "BOOKMARKS", Path("not-existing-path")):
        with pytest.raises(SystemExit):
            b.copy_bookmarks_file()

@patch.object(backup_mode, "datetime")
def test_get_current_datetime(mock_backup_mode: MagicMock|datetime):
    """test getting of current, correct formatted datetime
    - mock datetime.now() to return datetime object

    Args:
        mock_backup_mode (MagicMock | datetime): mocked module datetime
    """
    b = BackupMode()
    mock_backup_mode.now.return_value = datetime(1970, 1, 1, 0, 0, 0)
    assert b.get_current_datetime() == "700101_000000"