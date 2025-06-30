from typing import Dict

import pytest
from pytest import raises

from samples.calculadora_maluca.src.calculators.calculator_1 import Calculator1


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


@pytest.mark.calculator1
class TestCalculator1:

    @pytest.mark.parametrize(
        "number, expected_result",
        [
            (1, 14.25),
            (2, 14.95),
            (10, 22.67),
            (0, 13.59),
        ],
    )
    def test_calculate1_success(self, number, expected_result):
        mock_request = MockRequest(body={"number": number})
        calculator_1 = Calculator1()
        response = calculator_1.calculate(mock_request)

        assert "data" in response
        assert "calculator" in response["data"]
        assert "result" in response["data"]
        assert response["data"]["result"] == expected_result

    def test_calculate1_with_body_error(self):
        mock_request = MockRequest(body={"numbre": 1})
        calculator_1 = Calculator1()

        with raises(Exception) as exception:
            calculator_1.calculate(mock_request)
        assert "Bad formatted body" in str(exception.value)

    def test_calculate1_with_value_type_error(self):
        mock_request = MockRequest(body={"number": "a"})
        calculator_1 = Calculator1()

        with raises(Exception) as exception:
            calculator_1.calculate(mock_request)
        assert "Type not valid" in str(exception.value)

    def test_calculate1_with_negative_number_error(self):
        mock_request = MockRequest(body={"number": -5})
        calculator_1 = Calculator1()

        with raises(Exception) as exception:
            calculator_1.calculate(mock_request)
        assert "Not accepted negative number" in str(exception.value)
