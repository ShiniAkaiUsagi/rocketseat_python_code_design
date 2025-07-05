from samples.calculadora_maluca.src.calculators.calculator_3 import Calculator3
from samples.calculadora_maluca.src.drivers.numpy_handler import NumpyHandler


def calculator3_factory():
    numpy_handler = NumpyHandler()
    calc = Calculator3(numpy_handler)
    return calc
