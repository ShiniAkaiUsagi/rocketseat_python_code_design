from typing import Dict, List

import numpy as np
import pytest
from numpy import inf
from pytest import raises

from samples.calculadora_maluca.src.calculators.calculator_2 import Calculator2
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

    # A ideia é testarmos somente a calculadora, e não o comportamento do NumpyHandler


@pytest.mark.calculator2
class TestCalculator2:

    # Integração entre Calculator2 e NumpyHandler
    @pytest.mark.parametrize(
        "numbers_list, expected_result",
        [
            ([1.5, 2.3], 0.28),
            ([2.0, 3.4], 0.16),
            ([10.1, 6.9], 0.08),
            ([0.5], np.float64(inf)),
        ],
    )
    def test_calculate2_numpy_handler_integration(self, numbers_list, expected_result):
        mock_request = MockRequest(body={"numbers": numbers_list})
        calculator_2 = Calculator2(NumpyHandler())
        response = calculator_2.calculate(mock_request)

        assert isinstance(response, dict)
        assert response == {"data": {"calculator": 2, "result": expected_result}}

    def test_calculate2_success(self):
        mock_request = MockRequest(body={"numbers": [1.5, 2.3]})
        calculator_2 = Calculator2(MockDriverHandler())
        response = calculator_2.calculate(mock_request)

        assert isinstance(response, dict)
        assert response == {"data": {"calculator": 2, "result": 0.33}}

    def test_calculate2_with_body_error(self):
        mock_request = MockRequest(body={"numbre": 1})
        calculator_2 = Calculator2(MockDriverHandler())

        with raises(Exception) as exception:
            calculator_2.calculate(mock_request)
        assert "Bad formatted body" in str(exception.value)

    def test_calculate1_with_value_type_error(self):
        mock_request = MockRequest(body={"numbers": "a"})
        calculator_2 = Calculator2(MockDriverHandler())

        with raises(Exception) as exception:
            calculator_2.calculate(mock_request)
        assert "Type not valid" in str(exception.value)

    def test_calculate2_with_zero_number_error(self):
        mock_request = MockRequest(body={"numbers": [0.0]})
        calculator_2 = Calculator2(MockDriverHandler())

        with raises(Exception) as exception:
            calculator_2.calculate(mock_request)
        assert "Zero value is not accepted" in str(exception.value)

    def test_calculate2_with_negative_number_error(self):
        mock_request = MockRequest(body={"numbers": [-5]})
        calculator_2 = Calculator2(MockDriverHandler())

        with raises(Exception) as exception:
            calculator_2.calculate(mock_request)
        assert "Not accepted negative number" in str(exception.value)

    def test_calculate2_with_empty_list(self):
        mock_request = MockRequest(body={"numbers": []})
        calculator_2 = Calculator2(MockDriverHandler())

        with raises(Exception) as exception:
            calculator_2.calculate(mock_request)
        assert "Numbers list should not be empty" in str(exception.value)
