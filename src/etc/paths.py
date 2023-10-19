from pathlib import Path
import os
import sys

ROOT: Path = Path(os.path.dirname(sys.executable)) if getattr(sys, 'frozen', False) else Path(__file__).resolve().parent.parent.parent
"""path of root dir of repo"""

BOOKMARKS: Path = Path(os.environ['LocalAppData'], "Google", "Chrome", "User Data", "Default", "Bookmarks")
"""abs path of Bookmarks file containing Chrome bookmarks"""