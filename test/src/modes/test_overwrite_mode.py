from pathlib import Path

from src.modes.overwrite_mode import OverwriteMode


def test_init():
    """test init
    """
    o = OverwriteMode(Path("/dummy/path"))
    assert o.bookmarks_path == Path("/dummy/path")