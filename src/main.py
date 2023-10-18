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
    args = docopt(__doc__)

    # do stuff #
    print(f"hello world, entered args are {args.values()}")


if __name__=="__main__":
    main()
