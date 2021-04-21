
from datainnews_v2 import application

@application.route('/')
def index():
    return 'future home of news app'