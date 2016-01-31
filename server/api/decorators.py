import json
import traceback

from flask import make_response
from functools import wraps

response_header = { "Content-Type": "application/json; charset=utf-8" }

class WebException(Exception): pass

def api_wrapper(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        web_result = {}
        response = 200
        try:
            web_result = f(*args, **kwds)
        except WebException as error:
            response = 200
            web_result = { "success": 0, "message": str(error) }
        except Exception as error:
            response = 200
            traceback.print_exc()
            web_result = { "success": 0, "message": "Something went wrong!", "error": [ str(error), traceback.format_exc() ] }
        result = (json.dumps(web_result), response, response_header)
        response = make_response(result)

        return response
    return wrapper
