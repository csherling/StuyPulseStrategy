import json
import traceback

from flask import make_response
from functools import wraps

response_header = { "Content-Type": "application/json; charset=utf-8" }

class WebException(Exception):
    """
    Exception to be caught by api_wrapper to display a message to the user.

    See also
    --------
    api_wrapper

    Examples
    --------
    if password != confirm_password:
        raise WebException("Passwords do not match!")
    """
    pass

def api_wrapper(f):
    """
    Wrapper for api routes.

    Handles exceptions and returns relevant data in json for parsing.

    Examples
    -------
    @app.route("/", methods=["POST", "GET"])
    @api_wrapper
    def index():
        ...
    """
    @wraps(f)
    def wrapper(*args, **kwds):
        web_result = {}
        response = 200
        try:
            web_result = f(*args, **kwds)
        except WebException as error:
            # WebException was intentionally raised, and nothing fatal has occurred.
            response = 200
            web_result = { "success": 0, "message": str(error) }
        except Exception as error:
            # Exception was raised when trying to run the function.
            response = 200
            traceback.print_exc()
            web_result = { "success": 0, "message": "Something went wrong!", "error": [ str(error), traceback.format_exc() ] }
        result = (json.dumps(web_result), response, response_header)
        response = make_response(result)

        return response
    return wrapper
