from pathlib import Path
from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.modes.overwrite_mode import OverwriteMode


class TestOverwriteMode(TestCase):
    def setUp(self) -> None:
        self.dummy_file = Path(__file__).resolve()
            # filepath for testing is path of this test_ file
        self.o = OverwriteMode(self.dummy_file)

    def test_init(self):
        """test init
        """
        assert self.o.bookmarks_path == self.dummy_file

    @patch.object(OverwriteMode, "bookmarks_path_exists")
    def test_process_bookmarks_path_exists(self, mock_bookmarks_path_exists: MagicMock):
        # test case bookmarks_path_exists returns True #
        mock_bookmarks_path_exists.return_value = True
        

        # test case bookmarks_path_exists returns False #
        mock_bookmarks_path_exists.return_value = False



    def test_bookmarks_path_exists(self):
        """test function that checks whether specified file exists
        """
        # test case 1: return true #
        assert self.o.bookmarks_path_exists() == True

        # test case 2: return false #
        self.o.bookmarks_path = Path("/not/existing/path")
        assert self.o.bookmarks_path_exists() == False