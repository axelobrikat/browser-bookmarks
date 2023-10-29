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


def main():
    # get CLI input args #
    args = docopt(__doc__)
    print(args)

    # set CLI input args and check for validity #
    Args.set_cli_args(args)
    err_msg: str = Args.check_cli_args()
    if err_msg:
        Exc.exit(err_msg)
    ## HIER ERST EXC WERFEN? #############
    

#     func()
#     import sys
#     print(sys.argv[1:])
#     print(sys.argv)
#     print(args)
#     return args

# def func():
#     # do stuff #
#     print(f"hello world")
#     print(f"hello world2")
#     print(f"hello world3")


if __name__=="__main__":
    main()
