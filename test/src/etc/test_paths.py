from pathlib import Path

from src.etc.paths import ROOT

def test_ROOT():
    """test root directory of project, when it is no executable
    """
    assert ROOT == Path(__file__).resolve().parent.parent.parent.parent