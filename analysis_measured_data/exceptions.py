class InputNotValidException(Exception):
    """

    Exception class representing an input not valid error.

    Args:
        message (str): A descriptive error message.

    Attributes:
        message (str): A descriptive error message.

    """

    def __init__(self, message):
        self.message = message
