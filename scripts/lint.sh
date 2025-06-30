#!/bin/bash

poetry run python -B -m pytest --cache-clear

find . -type d \( \
    -name "htmlcov" \
\) -exec rm -rf {} +

find . -type f \( \
    -name "*.pyc" -o \
    -name "coverage.xml" -o \
    -name "report.xml" -o \
    -name "report.html" -o \
    -name ".coverage" \
\) -delete

poetry update -q
poetry run isort .
poetry run black .
poetry run flake8 . --statistics
poetry run bandit --recursive . -c pyproject.toml