class CPTracerException(Exception):
    """Base exception for the application."""
    pass

class UserNotFoundException(CPTracerException):
    """Raised when the Codeforces handle does not exist."""
    pass

class APIConnectionException(CPTracerException):
    """Raised when the network fails or Codeforces API is down."""
    pass