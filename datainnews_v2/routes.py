
from datainnews_v2 import application
from datainnews_v2.helper import get_new_articles
from flask import render_template
import pandas as pd
import datetime


@application.route('/')
def index():
    df_nepalitimes = pd.read_csv(
        "datainnews_v2/static/csvs/NepaliTimes_flask.csv",
        parse_dates=['created_at'])
    df_nepalitimes['Newspaper'] = "Nepali Times"


    
    df_kathmandupost = pd.read_csv(
        "datainnews_v2/static/csvs/KathmanduPost_flask.csv",
        parse_dates=['created_at'])
    df_kathmandupost['Newspaper'] = "The Kathmandu Post"


    df = df_nepalitimes.append([df_kathmandupost])
    df = df.groupby('Newspaper').sum().join(df.groupby('Newspaper').size().to_frame('News Articles'))
  
    df.rename({
        'level1_count': 'Level 1',
        'level2_count': 'Level 2',
        'level3_count': 'Level 3',
        'level_2_3_valid': 'Filtered Articles',
        }, inplace=True, axis=1)
    df.reset_index(inplace=True)
  
    df['Level 1 %'] = (100 * df['Level 1'] / df['News Articles'
                      ]).map('{:,.1f} %'.format)
    df['Level 2 %'] = (100 * df['Level 2'] / df['Filtered Articles'
                      ]).map('{:,.1f} %'.format)
    df['Level 3 %'] = (100 * df['Level 3'] / df['Filtered Articles'
                      ]).map('{:,.1f} %'.format)
    chart1 = [{'name': 'Level 1', 'data': df['Level 1'].tolist()},
              {'name': 'Total Articles', 'data': df['News Articles'
              ].tolist()}]
    chart2 = (df['Level 1'] / df['News Articles'] * 100).tolist()
    chart3 = [{'name': 'Level 2', 'data': df['Level 2'].tolist()},
              {'name': 'Total Articles', 'data': df['News Articles'
              ].tolist()}]
    chart4 = (df['Level 2'] / df['News Articles'] * 100).tolist()

    chart5 = [{'name': 'Level 3', 'data': df['Level 3'].tolist()},
              {'name': 'Total Articles', 'data': df['News Articles'
              ].tolist()}]
    chart6 = (df['Level 3'] / df['News Articles'] * 100).tolist()


    level1 = df[['Newspaper', 'News Articles', 'Level 1', 'Level 1 %']]
    column_names_level1 = level1.columns.values
    row_data_level1 = list(level1.values.tolist())
    
    level2 = df[['Newspaper', 'Level 2', 'Filtered Articles',
                'News Articles', 'Level 2 %']]
    column_names_level2 = level2.columns.values
    row_data_level2 = list(level2.values.tolist())

    level3 = df[['Newspaper', 'Level 3', 'Filtered Articles',
                'News Articles', 'Level 3 %']]
    column_names_level3 = level3.columns.values
    row_data_level3 = list(level3.values.tolist())

    newspapers = df['Newspaper'].tolist()
    
    content = {
        'total_articles': df['News Articles'].sum(),
        'newspapers':newspapers,
        'chart1':chart1,
        'chart2':chart2,
        'chart3':chart3,
        'chart4':chart4,
        'chart5':chart5,
        'chart6':chart6,
        'column_names_level1': column_names_level1,
        'row_data_level1': row_data_level1,
        'column_names_level2': column_names_level2,
        'row_data_level2': row_data_level2,
        'column_names_level3': column_names_level3,
        'row_data_level3': row_data_level3,
    }
    return render_template("index.html", **content) 