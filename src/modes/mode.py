import json
from abc import ABC, abstractmethod

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

    def load_bookmark_file(self) -> None:
        """read BOOKMARKS file, store content and check that it is dict type
        """
        try: 
            with open(BOOKMARKS, "r", encoding='utf-8') as f:
                self.bm_data = json.load(f)
        except Exception as e:
            Exc.exit(
                f"Cannot load bookmarks file {BOOKMARKS}."
                f"\n{e}"
            )

        if not self.check_bm_data_for_json():
            Exc.exit(
                f"Data specified in BOOKMARKS file has not the correct format."
                f"Check that is has JSON format."
            )

    def check_bm_data_for_json(self) -> bool:
        """check that BOOKMARKS file content is json format
        """
        if type(self.bm_data) == dict:
            return True
        return False