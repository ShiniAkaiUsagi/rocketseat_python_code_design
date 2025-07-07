# RocketSeat

Projeto criado como forma de fixar e avaliar os conhecimentos obtidos no módulo 4: "Introdução ao Design de Código".
[Desafio](Desafio.txt).


## Requisitos

- [Python 3.13](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [Docker Desktop](https://docs.docker.com/desktop/)

#### VSCode Extensions recomendadas:
- SQLite Viewer
- MySQL (database-client.com)

## Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/ShiniAkaiUsagi/rocketseat_python_code_design.git

# 2. Acesse a pasta do projeto
cd rocketseat_python_python_code_design

# 3. Execute o script de build para preparar as ferramentas e ambiente
sh scripts/build.sh

# O script executa:
# python.exe -m pip install --upgrade pip
# pip install -U poetry
# poetry self update
# poetry update
# poetry run pre-commit install

```
## Tests
PYTHONPATH=. poetry run pytest


## Calculadora maluca
PYTHONPATH=. poetry run python samples/calculadora_maluca/src/run.py

