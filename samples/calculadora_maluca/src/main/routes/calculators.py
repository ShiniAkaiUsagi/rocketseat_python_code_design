from flask import Blueprint, jsonify, request

from samples.calculadora_maluca.src.calculators.calculator_1 import Calculator1
from samples.calculadora_maluca.src.calculators.calculator_2 import Calculator2
from samples.calculadora_maluca.src.drivers.numpy_handler import NumpyHandler

calc_route_bp = Blueprint("calc_routes", __name__)


@calc_route_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
    """"""
    try:
        calc = Calculator1()
        response = calc.calculate(request=request)
        response["success"] = True
        return jsonify(response)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@calc_route_bp.route("/calculator/2", methods=["POST"])
def calculator_2():
    """"""
    try:
        numpy_handler = NumpyHandler()
        calc = Calculator2(numpy_handler)
        response = calc.calculate(request=request)
        response["success"] = True
        return jsonify(response)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})
