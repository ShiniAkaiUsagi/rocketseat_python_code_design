from samples.calculadora_maluca.src.calculators.calculator_1 import Calculator1
from samples.calculadora_maluca.src.calculators.calculator_2 import Calculator2
from samples.calculadora_maluca.src.calculators.calculator_3 import Calculator3
from samples.calculadora_maluca.src.calculators.calculator_4 import Calculator4
from samples.calculadora_maluca.src.main.factories.calculator1_factory import (
    calculator1_factory,
)
from samples.calculadora_maluca.src.main.factories.calculator2_factory import (
    calculator2_factory,
)
from samples.calculadora_maluca.src.main.factories.calculator3_factory import (
    calculator3_factory,
)
from samples.calculadora_maluca.src.main.factories.calculator4_factory import (
    calculator4_factory,
)


def test_calculator1_factory_returns_calculator1_instance():
    calc = calculator1_factory()
    assert isinstance(calc, Calculator1)


def test_calculator2_factory_returns_calculator2_instance():
    calc = calculator2_factory()
    assert isinstance(calc, Calculator2)


def test_calculator3_factory_returns_calculator3_instance():
    calc = calculator3_factory()
    assert isinstance(calc, Calculator3)


def test_calculator4_factory_returns_calculator4_instance():
    calc = calculator4_factory()
    assert isinstance(calc, Calculator4)
