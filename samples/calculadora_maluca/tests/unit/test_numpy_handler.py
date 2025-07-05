import pytest
from pytest import raises


@pytest.mark.NumpyHandler
class TestNumpyHandler:

    @pytest.mark.parametrize(
        "numbers, expected",
        [
            ([1.0, 2.0, 3.0, 4.0, 5.0], 1.4142135623730951),
            ([-5.0, -10.0, -15.0], 4.0824829),
        ],
    )
    def test_standard_derivation_valid_cases(self, numbers, expected, numpy_handler):
        result = numpy_handler.standard_derivation(numbers)
        assert pytest.approx(result, rel=1e-6) == expected

    def test_standard_derivation_with_identical_numbers(self, numpy_handler):
        result = numpy_handler.standard_derivation([10.0, 10.0, 10.0])
        assert result == 0.0

    def test_standard_derivation_with_invalid_types(self, numpy_handler):
        with raises(TypeError) as exception:
            numpy_handler.standard_derivation([1.0, "two", 3.0])
        assert "Todos os elementos da lista devem ser inteiros ou floats" in str(
            exception.value
        )

    def test_standard_derivation_with_empty_list(self, numpy_handler):
        with raises(ValueError) as exception:
            numpy_handler.standard_derivation([])
        assert "A lista de números não pode estar vazia" in str(exception.value)

    @pytest.mark.parametrize(
        "numbers, expected",
        [
            ([1.0, 2.0, 3.0, 4.0, 5.0], 2.0),
            ([-5.0, -10.0, -15.0], 16.66666),
        ],
    )
    def test_variance_valid_cases(self, numbers, expected, numpy_handler):
        result = numpy_handler.variance(numbers)
        assert pytest.approx(result, rel=1e-6) == expected

    def test_variance_with_invalid_types(self, numpy_handler):
        with raises(TypeError) as exception:
            numpy_handler.variance([1.0, "two", 3.0])
        assert "Todos os elementos da lista devem ser inteiros ou floats" in str(
            exception.value
        )

    def test_variance_with_empty_list(self, numpy_handler):
        with raises(ValueError) as exception:
            numpy_handler.variance([])
        assert "A lista de números não pode estar vazia" in str(exception.value)

    @pytest.mark.parametrize(
        "numbers, expected",
        [
            ([1.0, 2.0, 3.0], 2.0),
            ([-5.0, -10.0, -15.0], -10.0),
        ],
    )
    def test_average_valid_cases(self, numbers, expected, numpy_handler):
        result = numpy_handler.average(numbers)
        assert pytest.approx(result, rel=1e-6) == expected

    def test_average_with_invalid_types(self, numpy_handler):
        with raises(TypeError) as exception:
            numpy_handler.average([1.0, "two", 3.0])
        assert "Todos os elementos da lista devem ser inteiros ou floats" in str(
            exception.value
        )

    def test_average_with_empty_list(self, numpy_handler):
        with raises(ValueError) as exception:
            numpy_handler.average([])
        assert "A lista de números não pode estar vazia" in str(exception.value)
