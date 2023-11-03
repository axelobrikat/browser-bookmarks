import json

from src.modes.mode import Mode
from src.etc.paths import BOOKMARKS
from src.etc.exceptions import Exc
from src.bookmark_root import Root


class ShowMode(Mode):
    """show current browser bookmarks
    """
    def __init__(self) -> None:
        self.bm_data: dict[str, dict|str|int] = {}
        self.bm_bar: dict[str, dict] = {}
        self.roots: list[Root] = []

    def process_bookmarks(self) -> None:
        """entry function when this mode is selected by user
        """
        self.load_bookmark_file()
        self.create_bookmark_roots()
        for root in self.roots:
            root.output_name()
            root.output_children(root.content["children"])

    def load_bookmark_file(self) -> None:
        """read BOOKMARKS file, store content and check that it is dict type
        """
        try: 
            with open(BOOKMARKS, "r", encoding='utf-8') as f:
                self.bm_data = json.load(f)
        except Exception as e:
            Exc.exit(
                f"Cannot load bookmarks file {BOOKMARKS}"
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

    def create_bookmark_roots(self) -> None:
        """for each "root" in BOOKMARKS file,
        ... create Root object and append to list
        """
        for key, val in self.bm_data["roots"].items():
            self.roots.append(Root(key, val))
