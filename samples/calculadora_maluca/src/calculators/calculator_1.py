from typing import Dict

from flask import Request as FlaskRequest

from samples.calculadora_maluca.src.errors.http_unprocessable_entity import (
    HttpUnprocessableEntityError,
)


class Calculator1:

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)

        splitted_number = input_data / 3
        first_process_result = self.__first_process(splitted_number)
        second_process_result = self.__second_process(splitted_number)
        third_process_result = splitted_number

        final_result = (
            first_process_result + second_process_result + third_process_result
        )
        response = self.__format_response(final_result)

        return response

    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise HttpUnprocessableEntityError("Bad formatted body!")
        if not isinstance(body["number"], (int, float)):
            raise HttpUnprocessableEntityError("Type not valid. Expected int or float!")
        if body["number"] < 0:
            raise HttpUnprocessableEntityError("Not accepted negative number!")
        input_data = body["number"]
        return input_data

    def __first_process(self, first_number: float) -> float:
        first_part = (first_number / 4) + 7
        second_part = (first_part**2) * 0.257
        return second_part

    def __second_process(self, second_number: float) -> float:
        first_part = second_number**2.121
        second_part = (first_part / 5) + 1
        return second_part

    def __format_response(self, calc_result: float) -> Dict:
        return {"data": {"calculator": 1, "result": round(calc_result, 2)}}
