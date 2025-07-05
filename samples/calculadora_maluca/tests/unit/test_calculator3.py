from typing import Dict, List

import pytest
from pytest import raises

from samples.calculadora_maluca.src.calculators.calculator_3 import Calculator3
from samples.calculadora_maluca.src.drivers.interfaces.driver_handler_interface import (
    DriverHandlerInterface,
)
from samples.calculadora_maluca.src.drivers.numpy_handler import NumpyHandler


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        return 3  # apenas representação da classe, número aleatório

    def variance(self, numbers: List[float]) -> float:
        return 0.1  # apenas representação da classe, número aleatório

    # A ideia é testarmos somente a calculadora, e não o comportamento do NumpyHandler


@pytest.mark.calculator3
class TestCalculator3:

    # Integração entre Calculator3 e NumpyHandler
    @pytest.mark.parametrize(
        "numbers_list, expected_result",
        [
            ([1.5, 2.3], 3.45),
            ([0, 54], 0),
            ([2.0, 1], 2.0),
            ([6, -5], -30),
        ],
    )
    def test_calculate3_numpy_handler_integration(self, numbers_list, expected_result):
        mock_request = MockRequest(body={"numbers": numbers_list})
        calculator_3 = Calculator3(NumpyHandler())
        response = calculator_3.calculate(mock_request)

        assert isinstance(response, dict)
        assert response == {"data": {"calculator": 3, "result": expected_result}}

    def test_calculate3_success(self):
        mock_request = MockRequest(body={"numbers": [1.5, 2.3]})
        calculator_3 = Calculator3(MockDriverHandler())
        response = calculator_3.calculate(mock_request)

        assert isinstance(response, dict)
        assert response == {"data": {"calculator": 3, "result": 3.45}}

    def test_calculate3_with_body_error(self):
        mock_request = MockRequest(body={"numbre": 1})
        calculator_3 = Calculator3(MockDriverHandler())

        with raises(Exception) as exception:
            calculator_3.calculate(mock_request)
        assert "Bad formatted body" in str(exception.value)

    def test_calculate3_with_value_type_error(self):
        mock_request = MockRequest(body={"numbers": "a"})
        calculator_3 = Calculator3(MockDriverHandler())

        with raises(Exception) as exception:
            calculator_3.calculate(mock_request)
        assert "Type not valid" in str(exception.value)

    def test_calculate3_with_empty_list(self):
        mock_request = MockRequest(body={"numbers": []})
        calculator_3 = Calculator3(MockDriverHandler())

        with raises(Exception) as exception:
            calculator_3.calculate(mock_request)
        assert "Numbers list should not be empty" in str(exception.value)

    def test_calculate3_failed_with_variance_lower_than_multiplication(self):
        mock_request = MockRequest(body={"numbers": [10, 11]})
        calculator_3 = Calculator3(MockDriverHandler())

        with raises(Exception) as exception:
            calculator_3.calculate(mock_request)
        assert "Variance should not be greater than multiplication" in str(
            exception.value
        )
