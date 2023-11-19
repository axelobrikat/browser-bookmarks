import json
from abc import ABC, abstractmethod
from pathlib import Path

from src.etc.paths import BOOKMARKS
from src.etc.exceptions import Exc


class Mode(ABC):
    """abstract parent class to handle Modes
    """
    def __init__(self) -> None:
        self.bm_data: dict[str, dict|str|int] = {}

    @abstractmethod
    def process_bookmarks(self):
        pass # pragma: no cover

    def load_bookmark_file(self, bm_file: Path = BOOKMARKS) -> None:
        """read bookmarks file, store content and check that it is dict type

        Args:
            bm_file (Path, optional): path of bookmarks file. Defaults to BOOKMARKS.
        """
        try:
            with open(bm_file, "r", encoding='utf-8') as f:
                self.bm_data = json.load(f)
        except Exception as e:
            Exc.exit(
                f"Cannot load bookmarks file {bm_file}."
                f"\n{e}"
            )

        if not self.check_bm_data_for_json():
            Exc.exit(
                f"Data specified in bookmarks file {bm_file} has not the correct format."
                f"Check that is has JSON format."
            )

    def check_bm_data_for_json(self) -> bool:
        """check that bookmarks file content is json format
        """
        if type(self.bm_data) == dict:
            return True
        return False