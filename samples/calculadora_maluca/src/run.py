from samples.calculadora_maluca.src.main.server.server import app


def app_run(host, port, debug):
    app.run(host=host, port=port, debug=debug)


if __name__ == "__main__":
    app_run(host="127.0.0.1", port=3000, debug=True)
