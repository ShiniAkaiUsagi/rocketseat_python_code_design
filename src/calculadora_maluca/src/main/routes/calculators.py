from flask import Blueprint, jsonify, request
from src.calculadora_maluca.src.calculators.calculator_1 import Calculator1

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