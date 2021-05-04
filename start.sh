#!/bin/sh

#
# chmod +x start.sh
#
source env/bin/activate
export FLASK_APP=run.py
export FLASK_DEBUG=1
flask run