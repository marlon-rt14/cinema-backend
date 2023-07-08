from colorama import Fore
from http.client import BAD_REQUEST, NOT_FOUND, FORBIDDEN, UNAUTHORIZED

from .responses import success_response, bad_response

ERROR_HANDLER = {
    "ConnectionError": lambda error: bad_response(
        msg="Invalid or malformed endpoint", status=BAD_REQUEST, data=str(error)
    ),
    "MultipleResultsFound": lambda error: bad_response(
        msg="Multiple rows were found", status=NOT_FOUND, data=str(error)
    ),
    "NoResultFound": lambda error: bad_response(
        msg="No row was found", status=NOT_FOUND, data=str(error)
    ),
    "NotFound": lambda error: bad_response(
        msg="No result was found", status=NOT_FOUND, data=str(error)
    ),
    "DecodeError": lambda error: bad_response(
        msg="Invalid or malfored token", status=UNAUTHORIZED, data=str(error)
    ),
    "ExpiredSignatureError": lambda error: bad_response(
        msg="Token expired", status=UNAUTHORIZED, data=str(error)
    ),
    "InvalidSignatureError": lambda error: bad_response(
        msg="Invalid token", status=UNAUTHORIZED, data=str(error)
    ),
    "ValidationError": lambda error: bad_response(
        data=error.message, status=BAD_REQUEST, msg="Validation error"
    ),
    "defaultError": lambda error: bad_response(data=str(error)),
}


def error_handler(error):
    type_error = type(error).__name__
    print(error)
    print(
        Fore.RED + f"Error ==> {type_error} ",
        Fore.BLUE + "(Controlled)\n"
        if type_error in ERROR_HANDLER
        else Fore.YELLOW + "(Not Controlled)\n",
    )
    handler = (
        ERROR_HANDLER[type_error]
        if type_error in ERROR_HANDLER
        else ERROR_HANDLER["defaultError"]
    )
    return handler(error)
