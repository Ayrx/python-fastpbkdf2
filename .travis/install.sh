#!/bin/bash

set -e
set -x

pip install virtualenv

virtualenv ~/.venv
source ~/.venv/bin/activate
pip install tox coveralls
