
from datainnews_v2 import application
from datainnews_v2.helper import get_new_articles
from flask import render_template
import pandas as pd
import datetime


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


# @application.route('/<newspaper>')
# def nepalitimes(newspaper):
#     df = pd.read_csv(
#         "datainnews_v2/static/csvs/NepaliTimes.csv",
#         parse_dates=['created_at'],
#         usecols=['created_at', 'urls'])
#     since = df.created_at.max().strftime("%Y-%m-%d %H:%M:%S")
#     until = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     df_ = get_new_articles(
#         newspaper_username='NepaliTimes',
#         since=since,
#         until=until)
#     content = {
#         "table": df_.to_html(classes="table"),
#         "size": df_.shape[0],
#         "last_updated": df_.created_at.max()
#     }
#     return render_template("index.html", **content)
