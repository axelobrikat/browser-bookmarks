from src.etc.tree import Tree


class Root():
    """BOOKMARKS file can have multiple roots, 
    ... e.g. bookmark-bar, mobile-bookmarks etc.
    - this class is a representation of a bookmark root
    """    
    def __init__(self, root_name: str, content: dict) -> None:
        self.root_name: str = root_name
        self.content: dict = content
        self.name: str = self.content.get("name", "")
        self.tree: Tree = Tree()

    def __str__(self) -> str:
        return f"This is bookmark root: {self.root_name}."
    
    def output_name(self) -> None:
        """print name of Root instance
        """
        print("\n" + self.name)
    
    def output_children(self, children: list[dict]) -> None:
        """output bookmark children to cli

        Args:
            children (list[dict]): bookmark children
        """
        self.tree.level += 1

        for child in children:
            # print tree structure #
            self.tree.output_level_space()

            # print child name #
            self.print_child_name(child.get("name", None))

            # recursion for each child's child #
            self.output_grandchildren(child.get("children", None))

    def print_child_name(self, name: str | None):
        """print name if not None

        Args:
            name (str | None): name of bookmark
        """
        if name != None:
            print(name)

    def output_grandchildren(self, child: list[dict] | None):
        """if bookmark entry has children:
        - go into recursion with these children
        - after function call, decrese tree level

        Args:
            child (list[dict] | None): bookmark child
        """
        if child != None:
            self.output_children(child)
            self.tree.level -= 1


