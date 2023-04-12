"""
Custom exception definitions
"""


from app.lib.constants import DEFAULT_ERROR_MESSAGE


class FailedUserCredentials(Exception):
    """ Raise when user credentials are invalid """
    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class BlockedIPException(Exception):
    """ Raise when IP address is blocked temporarily """
    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class DBFetchFailureException(Exception):
    """ Raise when fetching the records from database fails. """

    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class DBRecordNotFound(Exception):
    """ Raise when no record exist based on query parameters. """

    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class DBMultipleRecordsFound(Exception):
    """ Raise when multiple records exists based on query parameters. """

    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class DBCreateRecordException(Exception):
    """ Raise while failed to create a new record in data base table"""

    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class DBUpdateRecordException(Exception):
    """ Raise while failed to update a existing record in data base table"""

    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class TokenExpiredException(Exception):
    """
    Raise when the reset token password is expired.
    """

    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class InvalidResetTokenException(Exception):
    """
    Raise when the reset token password is invalid.
    """

    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class DuplicateRecordException(Exception):
    """
    Raises when try to create duplicate record.
    """

    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class InvalidOrNoArugumentError(Exception):
    """
    Raise when an invalid parameter value is passed or no value passed to required argument.
    """
    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class SuspectedMaliciousIPError(Exception):
    """
    Raise when suspected activities were identified from a ip address.
    """
    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class JSONDataException(Exception):
    """ Raise when invalid JSON data"""

    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class UnauthorizedException(Exception):
    """ Raise when user is unauthorized"""

    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class InvalidDataFileException(Exception):
    """ Raise when data file is not valid"""

    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class InvalidDataException(Exception):
    """ Raise when the metadata is invalid or some data file is not having correct data"""

    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class S3AWSDownloadException(Exception):
    """ Raise when download from AWS S3 fails"""

    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class S3AWSUploadException(Exception):
    """ Raise when upload to AWS S3 fails"""

    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class ForbiddenActionException(Exception):
    """ Raise when an action is forbidden under certain condition"""

    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)