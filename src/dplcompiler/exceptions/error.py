from enum import Enum


class ErrorCode(Enum):
    UNEXPECTED_TOKEN = "Unexpected token"
    ID_NOT_FOUND = "Identifier not found"
    DUPLICATE_ID = "Duplicate id found"
    TYPE_ERROR = "Unsupported type(s) of operation"
    ZERO_DIVISION = "Zero division"


class Error(Exception):
    def __init__(
        self, error_code: ErrorCode = None, token=None, message: str = None
    ) -> None:
        self.error_code = error_code
        self.token = token
        self.message = f"{self.__class__.__name__}: {message}"


class TokenizeError(Error):
    pass


class ParserError(Error):
    pass


class SemanticError(Error):
    pass
