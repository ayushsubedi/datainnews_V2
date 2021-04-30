
from datainnews_v2 import application
from flask import request


@application.route('/')
def index():
    return 'future home of news app'

@application.route('/nepalitimes')
def nepalitimes():
    newspaper = request.endpoint
    return request.endpoint