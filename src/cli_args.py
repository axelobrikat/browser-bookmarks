from pathlib import Path

from src.etc.exceptions import Exc

class Args():
    """handle cli input args
    """
    show: bool = False
    backup: bool   = False
    overwrite: Path | None = Path()

    @classmethod
    def set_cli_args(cls, args: dict[str, str | bool | None ]):
        """set class vars

        Args:
            args (dict[str, str  |  bool ]): docopt cli input args
        """
        cls.show = args["-s"]
        cls.backup = args["-b"]
        cls.overwrite = Path(args["-o"]) if args["-o"] else None

    @classmethod
    def check_cli_args(cls):
        """check for validity of content of CLi input
        """
        cls.overwrite_path_exists()

    @classmethod
    def overwrite_path_exists(cls) -> bool:
        """check that path of file with Chrome Bookmarks exists
        """
        if cls.overwrite and not cls.overwrite.exists():
            raise FileNotFoundError(Exc.format_exc_msg(
                f"Cannot find specified path '{cls.overwrite}'."
            ))