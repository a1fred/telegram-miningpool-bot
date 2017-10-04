from typing import Union, Dict


class PoolInterfaceAbstract:
    """
    Abstract pool interface
    """

    command: str = None

    def __init__(self, *args, **kwargs):
        raise NotImplementedError

    def getBalance(self) -> Union[None, Dict[str, str]]:
        """
        returns:
           None: request has some errors
           Dict[str, str]: label: value pairs that returns to user
        """
        raise NotImplementedError
