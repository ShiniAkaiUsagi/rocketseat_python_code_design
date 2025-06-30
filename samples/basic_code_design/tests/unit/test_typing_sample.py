import pytest

from samples.basic_code_design.src.typing import (
    add,  # ajuste o import conforme seu projeto
)


@pytest.mark.typing_add
class TestAddFunction:

    @pytest.mark.parametrize(
        "elemento1, elemento2, expected_sum",
        [
            ("Hello,", " world!", "Hello, world!"),  # str + str
            (2, 3.5, 5.5),  # int + float
            (0, 0.0, 0.0),  # zeros
            (-1, 1.0, 0.0),  # negativo + positivo
            (1000000, 0.0001, 1000000.0001),  # grande + pequeno float
        ],
    )
    def test_add_valid_numbers(self, elemento1, elemento2, expected_sum):
        result = add(elemento1, elemento2)
        assert "sum" in result
        assert result["sum"] == pytest.approx(expected_sum)
