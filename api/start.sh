#!/bin/sh

python -m flask db init
python -m flask db migrate
python -m flask db upgrade
python -m flask run --host=0.0.0.0 --port=80
