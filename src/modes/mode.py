from abc import ABC, abstractmethod

class Mode(ABC):
    """abstract parent class to handle Modes
    """
    def __init__(self) -> None:
        pass # pragma: no cover

    @abstractmethod
    def process_bookmarks(self):
        pass # pragma: no cover