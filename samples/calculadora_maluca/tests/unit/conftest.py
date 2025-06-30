import pytest

from samples.calculadora_maluca.src.drivers.numpy_handler import NumpyHandler


@pytest.fixture
def numpy_handler():
    return NumpyHandler()
