from samples.calculadora_maluca.src.calculators.calculator_4 import Calculator4
from samples.calculadora_maluca.src.drivers.numpy_handler import NumpyHandler


def calculator4_factory():
    numpy_handler = NumpyHandler()
    calc = Calculator4(numpy_handler)
    return calc
