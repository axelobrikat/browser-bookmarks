from src.modes.mode import Mode
from src.bookmark_root import Root


class ShowMode(Mode):
    """show current browser bookmarks
    """
    def __init__(self) -> None:
        self.roots: list[Root] = []

    def process_bookmarks(self) -> None:
        """entry function when this mode is selected by user
        """
        self.load_bookmark_file()
        self.create_bookmark_roots()
        for root in self.roots:
            root.output_name()
            root.output_children(root.content["children"])

    def create_bookmark_roots(self) -> None:
        """for each "root" in BOOKMARKS file,
        ... create Root object and append to list
        """
        for key, val in self.bm_data["roots"].items():
            self.roots.append(Root(key, val))
