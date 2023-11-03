class Root():
    """BOOKMARKS file can have multiple roots, 
    ... e.g. bookmark-bar, mobile-bookmarks etc.
    - this class is a representation of a bookmark root
    """    
    def __init__(self, root_name: str, content: dict) -> None:
        self.root_name: str = root_name
        self.content: dict = content
        self.name: str = self.content.get("name", "")

    def __str__(self):
        return f"This is bookmark root: {self.root_name}."
    
    def output_name(self):
        """print name of Root isntance
        """
        print(self.name)
    
    def output_children(self, child: list[dict]):
        # print space + space*levelcounter
        # print tree ast
        # print children name
        # level_counter++
        # for c in child
          # output_children
          # level_coutner--
        return
