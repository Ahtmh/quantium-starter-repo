#!/bin/bash

. ./.venv/Scripts/activate

python -m pytest test_visualiser.py

PYTEST_EXIT_CODE=$?

if [ $PYTEST_EXIT_CODE -eq 0 ]
then
  exit 0
else
  exit 1
fi