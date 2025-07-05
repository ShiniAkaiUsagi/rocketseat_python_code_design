from typing import List

import numpy

from .interfaces.driver_handler_interface import DriverHandlerInterface


# Design Pattern Facade - Fachada
# Ao trabalhar com dependências externas, criamos essa classe de fachada para não precisar importar a mesma em diversos arquivos. Padronizamos assim o uso
# https://refactoring.guru/pt-br/design-patterns/facade
class NumpyHandler(DriverHandlerInterface):
    def __init__(self) -> None:
        self.__np = numpy

    def standard_derivation(self, numbers: List[float]) -> float:
        if not numbers:
            raise ValueError("A lista de números não pode estar vazia.")

        if not all(isinstance(n, (int, float)) for n in numbers):
            raise TypeError("Todos os elementos da lista devem ser inteiros ou floats.")

        return self.__np.std(numbers)

    def variance(self, numbers: List[float]) -> float:
        if not numbers:
            raise ValueError("A lista de números não pode estar vazia.")

        if not all(isinstance(n, (int, float)) for n in numbers):
            raise TypeError("Todos os elementos da lista devem ser inteiros ou floats.")

        return self.__np.var(numbers)

    def average(self, numbers: List[float]) -> float:
        if not numbers:
            raise ValueError("A lista de números não pode estar vazia.")

        if not all(isinstance(n, (int, float)) for n in numbers):
            raise TypeError("Todos os elementos da lista devem ser inteiros ou floats.")

        return self.__np.average(numbers)
