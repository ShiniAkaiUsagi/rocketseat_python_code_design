from unittest.mock import patch

import pytest
from flask import Flask

from samples.calculadora_maluca.src.main.routes.calculators import calc_route_bp


@pytest.fixture
def app():
    """Cria e configura a aplicação Flask com a rota a ser testada."""
    app = Flask(__name__)
    app.config["TESTING"] = True
    app.register_blueprint(calc_route_bp)
    return app


@pytest.fixture
def client(app):
    """Cria o cliente de teste para simular requisições HTTP."""
    return app.test_client()


@pytest.mark.routes
class TestCalculatorsRoutes:

    @patch("samples.calculadora_maluca.src.main.routes.calculators.calculator1_factory")
    def test_calculator_1_success(self, mock_calculator1, client):
        mock_instance = mock_calculator1.return_value
        mock_instance.calculate.return_value = {
            "data": {"calculator": 1, "result": 99.9}
        }

        response = client.post("/calculator/1", json={"number": 30})

        json_data = response.get_json()
        assert response.status_code == 200
        assert json_data["success"] is True
        assert "data" in json_data
        mock_instance.calculate.assert_called_once()

    @patch("samples.calculadora_maluca.src.main.routes.calculators.calculator1_factory")
    def test_calculator_1_failure(self, mock_calculator1, client):
        mock_instance = mock_calculator1.return_value
        mock_instance.calculate.side_effect = Exception("Erro calculadora 1")

        response = client.post("/calculator/1", json={"number": "abc"})

        # json_data = response.get_json()
        assert response.status_code == 500

    @patch(
        "samples.calculadora_maluca.src.main.routes.calculators.calculator2_factory.NumpyHandler"
    )
    @patch("samples.calculadora_maluca.src.main.routes.calculators.calculator2_factory")
    def test_calculator_2_success(self, mock_calculator2, mock_numpy_handler, client):
        mock_calc_instance = mock_calculator2.return_value
        mock_calc_instance.calculate.return_value = {
            "data": {"calculator": 2, "result": 12.34}
        }

        response = client.post("/calculator/2", json={"number": 9})

        json_data = response.get_json()
        assert response.status_code == 200
        assert json_data["success"] is True
        assert "data" in json_data
        mock_calc_instance.calculate.assert_called_once()

    @patch(
        "samples.calculadora_maluca.src.main.routes.calculators.calculator2_factory.NumpyHandler"
    )
    @patch("samples.calculadora_maluca.src.main.routes.calculators.calculator2_factory")
    def test_calculator_2_failure(self, mock_calculator2, mock_numpy_handler, client):
        mock_calc_instance = mock_calculator2.return_value
        mock_calc_instance.calculate.side_effect = Exception("Erro calculadora 2")

        response = client.post("/calculator/2", json={"number": 15})

        # json_data = response.get_json()
        assert response.status_code == 500

    @patch(
        "samples.calculadora_maluca.src.main.routes.calculators.calculator3_factory.NumpyHandler"
    )
    @patch("samples.calculadora_maluca.src.main.routes.calculators.calculator3_factory")
    def test_calculator_3_success(self, mock_calculator3, mock_numpy_handler, client):
        mock_calc_instance = mock_calculator3.return_value
        mock_calc_instance.calculate.return_value = {
            "data": {"calculator": 3, "result": 12.34}
        }

        response = client.post("/calculator/3", json={"number": 9})

        json_data = response.get_json()
        assert response.status_code == 200
        assert json_data["success"] is True
        assert "data" in json_data
        mock_calc_instance.calculate.assert_called_once()

    @patch(
        "samples.calculadora_maluca.src.main.routes.calculators.calculator3_factory.NumpyHandler"
    )
    @patch("samples.calculadora_maluca.src.main.routes.calculators.calculator3_factory")
    def test_calculator_3_failure(self, mock_calculator2, mock_numpy_handler, client):
        mock_calc_instance = mock_calculator2.return_value
        mock_calc_instance.calculate.side_effect = Exception("Erro calculadora 3")

        response = client.post("/calculator/3", json={"number": 15})

        # json_data = response.get_json()
        assert response.status_code == 500
