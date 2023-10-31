from pathlib import Path

from src.modes.mode import Mode


class OverwriteMode(Mode):
    def __init__(self, bookmarks_path: Path) -> None:
        self.bookmarks_path = bookmarks_path

    def process_bookmarks(self):
        """entry function when this mode is selected by user
        """
        #TODO: for cheksum etc, see
            # https://stackoverflow.com/questions/63105717/how-do-i-run-a-test-to-check-if-google-chrome-is-running-python
            # https://stackoverflow.com/questions/11308603/logic-behind-creating-bookmark-checksum-in-google-chrome
        pass