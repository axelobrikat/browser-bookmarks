import json

from src.etc.paths import BOOKMARKS


class Bib():
    def __init__(self) -> None:
        self.bm_data: dict = None

    def show_bookmarks(self):
        self.load_bookmark_file()

    def load_bookmark_file(self):
            with open(BOOKMARKS, "r", encoding='utf-8') as f:
                self.bm_data = json.load(f)
                print(self.bm_data)
                print(type(self.bm_data))


    def backup_bookmarks(self):
        pass

    def overwrite_bookmarks(self):
        pass

