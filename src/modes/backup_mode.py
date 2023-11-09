from pathlib import Path
from datetime import datetime
import shutil

from src.modes.mode import Mode
from src.etc.exceptions import Exc
from src.etc.paths import BOOKMARKS, ROOT


class BackupMode(Mode):
    """backup bookmarks file
    - copy, rename and save file to ./data
    """
    def __init__(self) -> None:
        self.dest_path: Path = ROOT / "data"
        self.dest_name: str = ""

    def process_bookmarks(self):
        """entry function when this mode is selected by user
        """
        self.copy_bookmarks_file()
    
    def copy_bookmarks_file(self):
        """copy bookmarks file to ./data as file yymmdd_HHMMSS_Backup_Bookmarks
        - print success message to cli, if successfully copied
        - otherwise, raise exception and exit program
        """
        try:
            self.dest_name: str = f"{self.get_current_datetime()}_Backup_Bookmarks"
            shutil.copyfile(
                BOOKMARKS,
                self.dest_path / self.dest_name
            )
            print(
                f"Copy of file {BOOKMARKS} successfully saved"
                f"\n as {self.dest_path / self.dest_name}."
            )
        except Exception as e:
            Exc.exit(
                f"Cannot create backup of bookmarks file."
                f"{e}"
            )

    def get_current_datetime(self) -> str:
        """return current datetime, format 'yymmdd_HHMMSS')

        Returns:
            str: current, formatted datetime
        """
        return datetime.now().strftime("%y%m%d_%H%M%S")