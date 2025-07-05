from typing import Dict, List

from flask import Request as FlaskRequest

from samples.calculadora_maluca.src.drivers.interfaces.driver_handler_interface import (
    DriverHandlerInterface,
)
from samples.calculadora_maluca.src.errors.http_bad_request import HttpBadRequestError
from samples.calculadora_maluca.src.errors.http_unprocessable_entity import (
    HttpUnprocessableEntityError,
)


class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        variance = self.__calculate_varianca(input_data)
        multiplication = self.__calculate_multiplication(input_data)

        self.__verify_results(variance, multiplication)
        formatted_response = self.__format_response(multiplication)
        return formatted_response

    def __validate_body(self, body: Dict) -> float:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Bad formatted body!")
        if not isinstance(body["numbers"], list):
            raise HttpUnprocessableEntityError("Type not valid. Expected int or float!")

        if not body["numbers"]:
            raise HttpUnprocessableEntityError("Numbers list should not be empty!")

        input_data = body["numbers"]
        return input_data

    def __calculate_varianca(self, numbers: List[float]) -> float:
        result = self.__driver_handler.variance(numbers)
        return 1 / result

    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication = 1
        for num in numbers:
            multiplication *= num

        return multiplication

    def __verify_results(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise HttpBadRequestError(
                "Variance should not be greater than multiplication!"
            )

    def __format_response(self, calculated_number: float) -> Dict:
        return {"data": {"calculator": 3, "result": round(calculated_number, 2)}}
