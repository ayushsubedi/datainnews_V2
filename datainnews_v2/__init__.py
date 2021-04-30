from flask import Flask
from os import environ
from os.path import join, dirname
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('english'))

application = Flask(__name__)

from datainnews_v2 import routes