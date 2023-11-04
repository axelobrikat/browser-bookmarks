from pytest import CaptureFixture
from unittest.mock import patch, MagicMock, call

from src.bookmark_root import Root
from src.etc.tree import Tree
from test.src.modes.test_show_mode import get_exp_bm_data_roots


def test_init():
    """test __init__ of Root class
    """
    # test case 1: no "name" in content dict #
    r = Root("test", {"foo": "bar"})
    assert r.root_name == "test"
    assert r.content == {"foo": "bar"}
    assert r.name == ""

    # test case 2: "name" in content dict #
    r = Root("test", {"name": "bar"})
    assert r.root_name == "test"
    assert r.content == {"name": "bar"}
    assert r.name == "bar"

def test_str():
    """test __str__ of Root class
    """
    r = Root("test", {"foo": "bar"})
    assert r.__str__() == "This is bookmark root: test."

def test_output_name(capsys: CaptureFixture):
    """test printing name to cli

    Args:
        capsys (CaptureFixture): captures output to cli
    """
    r = Root("test", {"name": "bar"})
    r.output_name()
    assert capsys.readouterr().out == (
        "\nbar\n"
    )

@patch.object(Tree, "output_level_space")
@patch.object(Root, "print_child_name")
@patch.object(Root, "output_grandchildren")
def test_output_children(
    mock_output_grandchildren: MagicMock,
    mock_print_child_name: MagicMock,
    mock_output_level_space: MagicMock,
):
    """test printing of bookmark children to cli

    Args:
        mock_output_grandchildren (Mock): mocked function
        mock_print_child_name (Mock): mocked function
        mock_output_level_space (Mock): mocked function
    """
    r = Root("bookmark_bar", get_exp_bm_data_roots()["roots"]["bookmark_bar"])
    r.tree.level = 0

    r.output_children(r.content["children"])

    assert r.tree.level == 1
    mock_output_level_space.call_count == 3
    assert mock_print_child_name.call_args_list == [
        call("tmp"),
        call("Outlook"),
        call("Dropbox"),
    ]
    assert mock_output_grandchildren.call_args_list == [
        call(r.content["children"][0]["children"]),
        call(None),
        call(None),
    ]

def test_print_child_name(capsys: CaptureFixture):
    """test printing children name to cli if name is not None

    Args:
        capsys (CaptureFixture): captures output to cli
    """
    r = Root("test", {})
    r.print_child_name("foo")
    assert capsys.readouterr().out == (
        "foo\n"
    )

def test_print_child_name_None(capsys: CaptureFixture):
    """test printing children name to cli if name is None

    Args:
        capsys (CaptureFixture): captures output to cli
    """
    r = Root("test", {})
    r.print_child_name(None)
    assert capsys.readouterr().out == ("")

@patch.object(Root, "output_children")
def test_output_grandchildren(mock_output_children: MagicMock):
    """test outputting grandchildren if child input arg is not None

    Args:
        mock_output_children (MagicMock): mocked function
    """
    r = Root("test", {})
    r.tree.level = 1
    test_child = [{"foo": "bar"}]
    r.output_grandchildren(test_child)
    assert mock_output_children.call_args(test_child)
    assert r.tree.level == 0

def test_output_grandchildren_None():
    """test outputting grandchildren if child input arg is None
    """
    r = Root("test", {})
    r.tree.level = 1
    r.output_grandchildren(None)
    assert r.tree.level == 1