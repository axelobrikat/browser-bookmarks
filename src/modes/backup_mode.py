from datetime import datetime
import shutil

from src.modes.mode import Mode
from src.etc.paths import BOOKMARKS


class BackupMode(Mode):
    """backup bookmarks file
    - copy, rename and save file to ./data
    """
    def __init__(self) -> None:
        self.now: datetime|None = None

    def process_bookmarks(self):
        """entry function when this mode is selected by user
        """
        pass
        # save_current_datetime()
        # transform_date() -> YYMMDD_HHmmss
          # with f"{str(self.now.year)[-2:]}..."
        # copy_bookmarks_file() 
          # with shutil.copyfile(src, dest)
          # print to cli that copied successful