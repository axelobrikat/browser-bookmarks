from pathlib import Path

from src.modes.mode import Mode
from src.etc.exceptions import Exc


class OverwriteMode(Mode):
    def __init__(self, bookmarks_path: Path) -> None:
        self.bookmarks_path: Path = bookmarks_path
        self.browser_bm_data: dict[str, dict|str|int] = {}

    def process_bookmarks(self):
        """entry function when this mode is selected by user
        """
        if not self.bookmarks_path_exists():
            Exc.exit(
                f"Specified file {self.bookmarks_path} for overwriting browser "
                f"bookmarks does not exist."
            )

        # load_bookmarks file and check for json structure
        # check loaded bookmarks file for "sync_metadata" - print warning - ask user to proceed anyway?
        # delete checksum ...
        #TODO: for cheksum etc, see
            # https://stackoverflow.com/questions/63105717/how-do-i-run-a-test-to-check-if-google-chrome-is-running-python
            # https://stackoverflow.com/questions/11308603/logic-behind-creating-bookmark-checksum-in-google-chrome
        # for [BOOKMARKS, bookmark_file] do load_and_check_bookmark_file

        # overwrite - ask user if not sure, whether he wants to do a backup

    def bookmarks_path_exists(self) -> bool:
        """check whether specified bookmarks file exists

        Returns:
            bool: True, if file exists, false if not
        """
        if self.bookmarks_path.is_file():
            return True
        return False