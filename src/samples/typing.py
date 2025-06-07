from typing import Dict

def add(elemento1: int, elemento2:float) -> Dict:
    response = elemento1 + elemento2
    return {"sum": response}

var1 = add(2.50, 3)
var2 = add('hello', ' world')
print(var1)
print(var2)
# Funciona, pois a tipagem é apenas um 'aconselhamento' do valor a ser utilizado

"""
Tipos de Tipagem:
# int, float, str, bool
# Dict, List, Tuple
# Objects

"""
