class Root():
    """BOOKMARKS file can have multiple roots, 
    ... e.g. bookmark-bar, mobile-bookmarks etc.
    - this class is a representation of a bookmark root
    """    
    def __init__(self, root_name: str) -> None:
        self.root_name: str = root_name

    def __str__(self):
        return f"This is bookmark root: {self.root_name}."