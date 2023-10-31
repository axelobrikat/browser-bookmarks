from src.cli_args import Args
from src.etc.exceptions import Exc
from src.modes.backup_mode import BackupMode
from src.modes.show_mode import ShowMode
from src.modes.overwrite_mode import OverwriteMode


class Orchestrator():
    """orchestrate actions
    """
    @classmethod
    def orchestrate_modes(cls):
        """orchestrate actions given by cli options
        """
        if Args.show:
            show_mode: ShowMode = ShowMode()
            show_mode.process_bookmarks()
        elif Args.backup:
            backup_mode: BackupMode = BackupMode()
            backup_mode.process_bookmarks()
        elif Args.overwrite:
            overwrite_mode: OverwriteMode = OverwriteMode(Args.overwrite)
            overwrite_mode.process_bookmarks()
        else:
            Exc.exit(
                f"No action has been specified on CLI as input argument."
            )