"""
Usage:
    main.py
"""
# """
# Usage:
#     main.py [-b | -o <file>]

# Options:
#     <>          show bookmarks of locally installed Chrome app
#     -b          backup: create backup of current Chrome bookmarks in ./data
#     -o <file>   overwrite: overwrite bookmarks of locally installed Chrome app with <file>
# """
# from docopt import docopt

# from src.cli_args import Args
from src.etc.paths import BOOKMARKS


# def main():
#     # get CLI input args #
#     args = docopt(__doc__)

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

def main():
    print(BOOKMARKS)


if __name__=="__main__":
    main()
