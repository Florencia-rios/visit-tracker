#!/bin/bash
cd src
echo "Installing dependencies..."
pip install -r ./visit-tracker/requirements.txt
export FLASK_APP=app.py
export FLASK_ENV=development
flask run

