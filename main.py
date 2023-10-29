"""
Usage:
    main.py (-s | -b | -o <file>)

Options:
    -s          show bookmarks of locally installed Chrome app
    -b          backup: create backup of current Chrome bookmarks in ./data
    -o <file>   overwrite: overwrite bookmarks of locally installed Chrome app with <file>
"""
from docopt import docopt

from src.cli_args import Args
from src.etc.exceptions import Exc
from src.etc.paths import BOOKMARKS
from src.orchestrate import Orchestrator


def main():
    """
    - get and process CLI input args
    - and start program
    """
    # get CLI input args #
    args = docopt(__doc__)

    # set CLI input args and check for validity #
    Args.set_cli_args(args)
    err_msg: str = Args.check_cli_args()
    if err_msg:
        Exc.exit(err_msg)

    # orchestrate modes #
    Orchestrator.orchestrate_modes()


if __name__=="__main__":
    main() # pragma: no cover
