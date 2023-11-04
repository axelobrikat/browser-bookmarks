class Tree():
    """output bookmarks in BOOKMARKS file as tree
    """
    def __init__(self) -> None:
        self.strike: str = "_"
        self.pipe: str = "|"
        self.space: str = " "
        self.level: int = -1

    def output_level_space(self) -> None:
        print(self.level*self.space*4 + self.pipe + 3*self.strike, end="")