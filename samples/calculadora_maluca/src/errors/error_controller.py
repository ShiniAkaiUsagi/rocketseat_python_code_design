from typing import Dict

from samples.calculadora_maluca.src.errors.http_bad_request import HttpBadRequestError
from samples.calculadora_maluca.src.errors.http_unprocessable_entity import (
    HttpUnprocessableEntityError,
)


def handle_errors(error: Exception) -> Dict:
    if isinstance(error, (HttpUnprocessableEntityError, HttpBadRequestError)):
        return {
            "status_code": error.status_code,
            "body": {"error": [{"title": error.name, "detail": error.message}]},
        }
    return {
        "status_code": 500,
        "body": {"error": [{"title": "Server Error", "detail": str(error)}]},
    }
