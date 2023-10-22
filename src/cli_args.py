class Args():
    """handle cli input args
    """
    show: str = ''
    backup: str = ''
    overwrite: str = ''

    @classmethod
    def set_cli_args(cls, args: dict[str, str | bool ]):
        """set class vars

        Args:
            args (dict[str, str  |  bool ]): docopt cli input args
        """
        cls.show = args["-s"]
        cls.backup = args["-b"]
        cls.overwrite= args["-o"]