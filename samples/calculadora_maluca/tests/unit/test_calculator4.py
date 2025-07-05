from typing import Dict, List

import pytest
from pytest import raises

from samples.calculadora_maluca.src.calculators.calculator_4 import Calculator4
from samples.calculadora_maluca.src.drivers.interfaces.driver_handler_interface import (
    DriverHandlerInterface,
)
from samples.calculadora_maluca.src.drivers.numpy_handler import NumpyHandler


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        pass  # apenas representação da classe

    def variance(self, numbers: List[float]) -> float:
        pass  # apenas representação da classe

    def average(self, numbers: List[float]) -> float:
        return 5  # apenas representação da classe, número aleatório

    # A ideia é testarmos somente a calculadora, e não o comportamento do NumpyHandler


@pytest.mark.calculator4
class TestCalculator4:

    @pytest.mark.parametrize(
        "numbers_list, expected_result",
        [
            ([1.5, 2.3], 1.9),
            ([2.0, 3.4], 2.7),
            ([-10.1, 6.9], -1.6),
            ([0.5, 0], 0.25),
        ],
    )
    def test_calculate4_numpy_handler_integration(self, numbers_list, expected_result):
        mock_request = MockRequest(body={"numbers": numbers_list})
        calculator_4 = Calculator4(NumpyHandler())
        response = calculator_4.calculate(mock_request)

        assert isinstance(response, dict)
        assert response == {"data": {"calculator": 4, "result": expected_result}}

    def test_calculate4_success(self):
        mock_request = MockRequest(body={"numbers": [1.5, 2.3]})
        calculator_4 = Calculator4(MockDriverHandler())
        response = calculator_4.calculate(mock_request)

        assert isinstance(response, dict)
        assert response == {"data": {"calculator": 4, "result": 5}}

    def test_calculate4_with_body_error(self):
        mock_request = MockRequest(body={"numbre": 1})
        calculator_4 = Calculator4(MockDriverHandler())

        with raises(Exception) as exception:
            calculator_4.calculate(mock_request)
        assert "Bad formatted body" in str(exception.value)

    def test_calculate4_with_value_type_error(self):
        mock_request = MockRequest(body={"numbers": "a"})
        calculator_4 = Calculator4(MockDriverHandler())

        with raises(Exception) as exception:
            calculator_4.calculate(mock_request)
        assert "Type not valid" in str(exception.value)

    def test_calculate4_with_less_than_two_numbers(self):
        mock_request = MockRequest(body={"numbers": [0.0]})
        calculator_4 = Calculator4(MockDriverHandler())

        with raises(Exception) as exception:
            calculator_4.calculate(mock_request)
        assert "At least two numbers are required to calculate the average" in str(
            exception.value
        )

    def test_calculate4_with_empty_list(self):
        mock_request = MockRequest(body={"numbers": []})
        calculator_4 = Calculator4(MockDriverHandler())

        with raises(Exception) as exception:
            calculator_4.calculate(mock_request)
        assert "Numbers list should not be empty" in str(exception.value)
