class AppError(Exception):
    """Raised by services; main.py turns it into a JSON response."""

    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

        """This defines a custom exception that your service layer raises for expected errors (bad input, not found, unauthorized, etc.), so route handlers don’t have to build error responses themselves.

How it works

AppError inherits from Exception, so you can raise it like any other error.
message is the human-readable error text.
status_code is the HTTP status to return, defaulting to 400 (Bad Request).
super().__init__(message) keeps normal exception behavior, so str(error) and tracebacks show the message."""
