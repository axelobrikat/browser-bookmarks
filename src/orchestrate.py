from src.cli_args import Args
from src.etc.exceptions import Exc
from src.bib import Bib


class Orchestrator():
    """orchestrate actions
    """
    bib: Bib = Bib()

    @classmethod
    def orchestrate_modes(cls):
        """orchestrate actions given by cli options
        """
        if Args.show:
            cls.bib.show_bookmarks()
        elif Args.backup:
            cls.bib.backup_bookmarks()
        elif Args.overwrite:
            cls.bib.overwrite_bookmarks()
        else:
            Exc.exit(
                f"No action has been specified on CLI as input argument."
            )