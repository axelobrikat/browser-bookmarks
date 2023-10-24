import sys

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
            f"\nError occured, Program end"
            f"\n============"
            f"\n{msg}"
            f"\n============\n"
        )
    
    @classmethod
    def exit(cls, msg: str):
        """exit program, as error occured and print info

        Args:
            msg (str): error message
        """
        sys.exit(cls.format_exc_msg(msg))