"""
Validation Methods
"""

from abc import ABC
from functools import wraps
from http import HTTPStatus

from cerberus import Validator, errors
from flask import jsonify, request
from jsonschema import draft4_format_checker
from jsonschema import validate, ValidationError


class CustomErrorHandler(errors.BasicErrorHandler, ABC):
    def __init__(self, schema):
        super(CustomErrorHandler, self).__init__()
        self.custom_defined_schema = schema

    def _format_message(self, field, error):
        error_msg = self.custom_defined_schema[field].get('meta', {}).get('custom_message', {}).get(error.rule)
        if error_msg:
            return error_msg
        return super(CustomErrorHandler, self)._format_message(field, error)


def validate_json_schema(schema, allow_unknown=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                validator = Validator(schema, error_handler=CustomErrorHandler(schema))
                validator.allow_unknown = allow_unknown
                is_valid = validator.validate(request.json_data)
                if not is_valid:
                    return jsonify({"status": "Invalid JSON", "errors": validator.errors}), HTTPStatus.UNPROCESSABLE_ENTITY
            except Exception as ex:
                import traceback
                traceback.print_exc()
                return jsonify({"status": "error", "message": str(ex)}), HTTPStatus.INTERNAL_SERVER_ERROR
            return func(*args, **kwargs)
        return wrapper
    return decorator


def validate_args_input(schema):
    def decorator(view_method):
        @wraps(view_method)
        def wrapper(*args, **kwargs):
            error = None
            try:
                validate(request.args, schema,
                         format_checker=draft4_format_checker)
            except ValueError as err:
                error = str(err)
            except ValidationError as err:
                error = err.message
            if error is not None:
                return jsonify({"status": "Invalid Args", "errors": error}), HTTPStatus.UNPROCESSABLE_ENTITY
            return view_method(*args, **kwargs)
        return wrapper
    return decorator
