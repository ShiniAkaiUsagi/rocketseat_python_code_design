import pytest

from samples.calculadora_maluca.src.main.server.server import app
from samples.calculadora_maluca.src.run import app_run


@pytest.mark.server_tests
class TestAppRun:

    def test_app_run_calls_flask_run(self, mocker):
        """
        Testa se a função app_run chama app.run com os parâmetros corretos,
        sem iniciar o servidor Flask real.
        """
        # Faz patch no método app.run para não iniciar o servidor real
        mock_run = mocker.patch.object(app, "run")

        # Chama a função que queremos testar
        app_run(host="127.0.0.1", port=5000, debug=True)

        # Verifica se app.run foi chamado com os parâmetros corretos
        mock_run.assert_called_once_with(host="127.0.0.1", port=5000, debug=True)
