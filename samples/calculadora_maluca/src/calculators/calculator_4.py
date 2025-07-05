from typing import Dict, List

from flask import Request as FlaskRequest

from samples.calculadora_maluca.src.drivers.interfaces.driver_handler_interface import (
    DriverHandlerInterface,
)
from samples.calculadora_maluca.src.errors.http_unprocessable_entity import (
    HttpUnprocessableEntityError,
)


class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        average = self.__calculate_average(input_data)

        formatted_response = self.__format_response(average)
        return formatted_response

    def __validate_body(self, body: Dict) -> float:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Bad formatted body!")
        if not isinstance(body["numbers"], list):
            raise HttpUnprocessableEntityError("Type not valid. Expected int or float!")

        if not body["numbers"]:
            raise HttpUnprocessableEntityError("Numbers list should not be empty!")

        if len(body["numbers"]) < 2:
            raise HttpUnprocessableEntityError(
                "At least two numbers are required to calculate the average!"
            )

        input_data = body["numbers"]
        return input_data

    def __calculate_average(self, numbers: List[float]) -> float:
        return self.__driver_handler.average(numbers)

    def __format_response(self, calculated_number: float) -> Dict:
        return {"data": {"calculator": 4, "result": round(calculated_number, 2)}}
