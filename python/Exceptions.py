class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class RangeError(Error):
    """Exception raised if accessed index is outside allowed range
    
    Attributes
    ----------
        message : str 
            explanation of the error
    
    """

    def __init__(self, message):
        self.message = message