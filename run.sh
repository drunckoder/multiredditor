#!/bin/bash
source venv/bin/activate
export PYTHONPATH=$PYTHONPATH:multiredditor
gunicorn -c gunicorn.py.ini multiredditor:app