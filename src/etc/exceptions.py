class Exc():
    """handle exceptions
    """
    @classmethod
    def format_exc_msg(cls, msg: str) -> str:
        """format exception message

        Args:
            msg (str): exception message

        Returns:
            str: formatted exception message
        """
        return (
            f"\n============"
            f"\n{msg}"
            f"\n============\n"
        )