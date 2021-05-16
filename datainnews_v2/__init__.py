from flask import Flask
from os import environ
from os.path import join, dirname


application = Flask(__name__)

from datainnews_v2 import routes