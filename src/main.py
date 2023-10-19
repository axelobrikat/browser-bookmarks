"""
Usage:
    main.py [-v | --verbose | -vv | -q | --quiet | -qq ]

Options:
    -v --verbose              verbosity: print more text (-v or --verbose -> INFO, -vv -> DEBUG)
    -q --quiet                verbosity: print less text (-q or --quiet -> ERROR, -qq -> CRITICAL)
                                - default verbosity: only print WARNINGS, ERRORS and CRITICALS (level -> WARNING)

"""
from docopt import docopt


def main():
    # get optional input command line args #
    print(__doc__)
    args = docopt(__doc__)

    func()
    import sys
    print(sys.argv[1:])
    print(sys.argv)
    print(args)
    return args

def func():
    # do stuff #
    print(f"hello world")
    print(f"hello world2")
    print(f"hello world3")


if __name__=="__main__":
    main()
