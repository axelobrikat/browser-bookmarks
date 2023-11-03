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

#####################
# hier einhaken, neben bookmark bar gibt es noch mehr roots
# ROOTS Klasse erstellen und hier durch so viele instanzen
# ... anlegen, wie bookmarks file hergibt
# danach durch iterieren und roots' children outputen
#####################
        self.create_bookmark_roots()

        return
        self.save_bookmark_bar()
        self.output_bookmarks()

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

    def save_bookmark_bar(self) -> None:
        """save bookmark_bar from read in BOOKMARK file
        """
        try:
            self.bm_bar = self.bm_data["roots"]["bookmark_bar"]
        except Exception as e:
            Exc.exit(
                f"Cannot find 'roots'->'bookmark_bar' in Bookmarks file {BOOKMARKS}."
                f"\nMake sure you specified the correct file."
                f"\n{e}"
            )

    def output_bookmarks(self) -> None:
        """output bookmarks to CLI
        """
        self.output_head()
        self.parse_bm_bar_children()
        self.output_bm_bar_children()

    def output_head(self) -> None:
        """output head of bookmarks: bookmark_bar
        """
        print(self.bm_bar["name"])

    def parse_bm_bar_children(self) -> None:
        pass

    def output_bm_bar_children(self) -> None:
        pass



    def show_bookmarks(self):
        self.print_bm_bar()
        self.print_children(self.bm_bar["children"])


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