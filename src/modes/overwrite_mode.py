from pathlib import Path

from src.modes.mode import Mode


class OverwriteMode(Mode):
    def __init__(self, bookmarks_path: Path) -> None:
        self.bookmarks_path: Path = bookmarks_path

    def process_bookmarks(self):
        """entry function when this mode is selected by user
        """
        #TODO: for cheksum etc, see
            # https://stackoverflow.com/questions/63105717/how-do-i-run-a-test-to-check-if-google-chrome-is-running-python
            # https://stackoverflow.com/questions/11308603/logic-behind-creating-bookmark-checksum-in-google-chrome
        pass

    def bookmarks_path_exists(self) -> bool:
        """check whether specified bookmarks file exists

        Returns:
            bool: True, if file exists, false if not
        """        
        if self.bookmarks_path.is_file():
            return True
        return False