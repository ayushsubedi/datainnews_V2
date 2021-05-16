
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
    df_nepalitimes = pd.read_csv(
        "datainnews_v2/static/csvs/NepaliTimes_flask.csv",
        parse_dates=['created_at'])
    df_nepalitimes['Newspaper'] = "Nepali Times"


    
    df_kathmandupost = pd.read_csv(
        "datainnews_v2/static/csvs/KathmanduPost_flask.csv",
        parse_dates=['created_at'])
    df_kathmandupost['Newspaper'] = "Kathmandu Post"


    df = df_nepalitimes.append([df_kathmandupost])
    df = df.groupby('Newspaper').sum().join(df.groupby('Newspaper').size().to_frame('News Articles'))
  
    df.rename({
        'level1_count': 'Level1',
        'level2_count': 'Level2',
        'level3_count': 'Level3',
        'level_2_3_valid': 'Filtered Articles',
        }, inplace=True, axis=1)
    df.reset_index(inplace=True)
  
    df['Level1 %'] = (100 * df['Level1'] / df['News Articles'
                      ]).map('{:,.1f} %'.format)
    df['Level2 %'] = (100 * df['Level2'] / df['Filtered Articles'
                      ]).map('{:,.1f} %'.format)
    df['Level3 %'] = (100 * df['Level3'] / df['Filtered Articles'
                      ]).map('{:,.1f} %'.format)
    chart1 = [{'name': 'Level 1', 'data': df['Level1'].tolist()},
              {'name': 'Total Articles', 'data': df['News Articles'
              ].tolist()}]
    chart2 = (df['Level1'] / df['News Articles'] * 100).tolist()

    level1 = df[['Newspaper', 'News Articles', 'Level1', 'Level1 %']]
    column_names_level1 = level1.columns.values
    row_data_level1 = list(level1.values.tolist())

    newspapers = df['Newspaper'].tolist()
    
    content = {
        'total_articles': df['News Articles'].sum(),
        'newspapers':newspapers,
        'chart1':chart1,
        'chart2':chart2,
        'column_names_level1': column_names_level1,
        'row_data_level1': row_data_level1,
    }
    return render_template("index.html", **content) 