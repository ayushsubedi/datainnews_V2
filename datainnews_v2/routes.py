
from datainnews_v2 import application
from flask import request, render_template
import pandas as pd


@application.route('/')
def index():
    df = pd.read_csv(
        "datainnews_v2/static/csvs/NepaliTimes.csv",
        parse_dates=['created_at'],
        usecols=['created_at', 'urls'])
    df.sort_values(['created_at'], inplace=True)
    content = {
        "table": df.tail().to_html(classes="table"),
        "size": df.shape[0],
        "last_updated": df.created_at.max()
    }
    return render_template("index.html", **content)


@application.route('/nepalitimes')
def nepalitimes():
    newspaper = request.endpoint
    return newspaper
