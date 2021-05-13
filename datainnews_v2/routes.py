
from datainnews_v2 import application
from datainnews_v2.helper import get_new_articles
from flask import render_template
import pandas as pd
import datetime


@application.route('/demo')
def demo():
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
    return render_template("demo.html", **content)


@application.route('/')
def index():
    return render_template("index.html") 