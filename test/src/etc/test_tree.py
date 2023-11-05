from pytest import CaptureFixture

from src.etc.tree import Tree


def test_output_level_space(capsys: CaptureFixture):
    """test outputting tree structure

    Args:
        capsys (CaptureFixture): capture stdout and stderr
    """
    tree = Tree()
    tree.level = 2
    tree.output_level_space()
    assert capsys.readouterr().out == (
        "        |___"
    )