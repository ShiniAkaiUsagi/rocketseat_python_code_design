from typing import Dict, List

from flask import Request as FlaskRequest

from samples.calculadora_maluca.src.drivers.interfaces.driver_handler_interface import (
    DriverHandlerInterface,
)


class Calculator2:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        result = self.__process_data(input_data)
        formatted_response = self.__format_response(result)
        return formatted_response

    def __validate_body(self, body: Dict) -> float:
        if "numbers" not in body:
            raise ValueError("Bad formatted body!")
        if not isinstance(body["numbers"], list):
            raise TypeError("Type not valid. Expected int or float!")

        if not body["numbers"]:
            raise TypeError("Numbers list should not be empty!")

        for number in body["numbers"]:
            if number == 0:
                raise ValueError("Zero value is not accepted for this calculator!")
            if number < 0:
                raise ValueError("Not accepted negative number!")
        input_data = body["numbers"]
        return input_data

    def __process_data(self, input_data: List[float]) -> float:
        first_process_result = [(num * 11) ** 0.95 for num in input_data]
        result = self.__driver_handler.standard_derivation(first_process_result)
        return 1 / result

    def __format_response(self, calculated_number: float) -> Dict:
        return {"data": {"calculator": 2, "result": round(calculated_number, 2)}}
