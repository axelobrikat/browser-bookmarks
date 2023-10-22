from src.cli_args import Args
from main import __doc__

def test_set_cli_args():
    """test setting of CLI input args
    """
    args: dict[str, str] = {
        '-b': False,
        '-o': 'dummy',
        '-s': False,
    }
    Args.set_cli_args(args)
    assert Args.show == False
    assert Args.backup == False
    assert Args.overwrite == 'dummy'