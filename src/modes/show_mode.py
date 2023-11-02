import json

from src.modes.mode import Mode
from src.etc.paths import BOOKMARKS
from src.etc.exceptions import Exc


class ShowMode(Mode):
    """show current browser bookmarks
    """
    def __init__(self) -> None:
        self.bm_data: dict[str, dict|str|int] = {}
        self.bm_bar: dict[str, dict] = {}

    def process_bookmarks(self):
        """entry function when this mode is selected by user
        """
        self.load_bookmark_file()
        self.get_bookmark_bar()

    def show_bookmarks(self):
        self.print_bm_bar()
        self.print_children(self.bm_bar["children"])

    def get_bookmark_bar(self):
        try:
            self.bm_bar = self.bm_data["roots"]["bookmark_bar"]
        except Exception as e:
            Exc.exit(
                f"Cannot find 'roots'->'bookmark_bar' in Bookmarks file {BOOKMARKS}."
                f"\nMake sure you specified the correct file."
                f"\n{e}"
            )


    def print_bm_bar(self):
        print(self.bm_bar["name"])

    def print_children(self, childs: list[dict]):
        for child in childs:
            print(child)
            if child != "children":
                continue
            c: list[dict] = child.get("children")
            if c != None:
                self.print_children(c)

        # for key, val in self.bm_data["roots"]["bookmark_bar"].items():
        #     print(key)
        #     print(type(key))
        #     print(type(val))

        #     # print(val)
        #     print()
# checksum
# roots
# sync_metadata
# version

    def load_bookmark_file(self):
        """read BOOKMARKS file and store content
        """
        try: 
            with open(BOOKMARKS, "r", encoding='utf-8') as f:
                self.bm_data = json.load(f)
        except Exception as e:
            Exc.exit(
                f"Cannot load bookmarks file {BOOKMARKS}"
                f"\n{e}"
            )