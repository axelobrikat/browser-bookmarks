"""
Note, this test file presents different approaches for unit testing python files
"""
from pytest_mock import MockerFixture
from unittest.mock import MagicMock, patch, Mock, call
import unittest
import pytest
from pathlib import Path

from src.etc.paths import ROOT, BOOKMARKS
from src.modes.show_mode import ShowMode
from src.modes import show_mode
from src.etc.exceptions import Exc
from src.bookmark_root import Root



@patch.object(ShowMode, "load_bookmark_file")
@patch.object(ShowMode, "create_bookmark_roots")
@patch.object(Root, "output_name")
@patch.object(Root, "output_children")
def test_process_bookmarks_with_roots(
   mock_output_children: Mock,
   mock_output_name: Mock,
   mock_create_bookmark_roots: Mock,
   mock_load_bookmark_file: Mock,
   ):
   """test function calls in output_bookmarks-function

   Args:
       mock_output_children (Mock): mocked function
       mock_output_name (Mock): mocked function
       mock_create_bookmark_roots (Mock): mocked function
       mock_load_bookmark_file (Mock): mocked function
   """
   sm = ShowMode()
   exp_call: dict = {"foo": "bar"}
   sm.roots = [
      Root("bar", {"children": exp_call}),
      Root("baz", {"children": exp_call}),
   ]
   sm.process_bookmarks()
   mock_load_bookmark_file.assert_called_once()
   mock_create_bookmark_roots.assert_called_once()
   assert mock_output_name.call_count == 2
   mock_output_name.assert_called()
   assert mock_output_children.call_count == 2
   assert mock_output_children.call_args_list == [
      call(exp_call),
      call(exp_call),
   ]

@patch.object(ShowMode, "load_bookmark_file")
@patch.object(ShowMode, "create_bookmark_roots")
@patch.object(Root, "output_name")
def test_process_bookmarks_without_roots(
   mock_output_name: Mock,
   mock_create_bookmark_roots: Mock,
   mock_load_bookmark_file: Mock,
   ):
   """test funcion calls in output_bookmarks function

   Args:
       mock_output_name (Mock): mocked function
       mock_create_bookmark_roots (Mock): mocked function
       mock_load_bookmark_file (Mock): mocked function
   """
   sm = ShowMode()
   sm.process_bookmarks()
   mock_load_bookmark_file.assert_called_once()
   mock_create_bookmark_roots.assert_called_once()
   mock_output_name.assert_not_called()



class TestShowMode(unittest.TestCase):
   """test show_mode.py with already read in bookmarks (dict)
   """
   def setUp(self) -> None:
      self.show_modes: ShowMode = ShowMode()


   def test_check_bm_data_for_json(self):
      """test type-checking of bm_data
      """
      # test case 1: bm_data is dict #
      self.show_modes.bm_data = {}
      assert self.show_modes.check_bm_data_for_json() == True

      # test case 2: bm_data is not dict #
      self.show_modes.bm_data = 0
      assert self.show_modes.check_bm_data_for_json() == False


   def test_create_bookmark_roots(self):
      """test creation of roots in BOOKMARKS file as separate Root instances
      """
      exp_roots: list[str] = [
         "foo",
         "bar",
         "baz",
      ]
      exp_contents: list[dict[str,int]] = [
         {"f":0},
         {"b":1},
         {"b":2},
      ]
      self.show_modes.bm_data: dict[str, dict] = {
         "roots": {
            exp_roots[0]: exp_contents[0],
            exp_roots[1]: exp_contents[1],
            exp_roots[2]: exp_contents[2],
         }
      }

      self.show_modes.create_bookmark_roots()

      for root in self.show_modes.roots:
         assert root.root_name in exp_roots
         assert root.content in exp_contents