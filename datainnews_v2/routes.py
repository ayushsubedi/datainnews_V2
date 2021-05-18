
from datainnews_v2 import application
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

    df_onlinekhabar = pd.read_csv(
        "datainnews_v2/static/csvs/OnlineKhabar_En_flask.csv",
        parse_dates=['created_at'])
    df_onlinekhabar['Newspaper'] = "Onlinekhabar"

    df_republicanepal = pd.read_csv(
        "datainnews_v2/static/csvs/RepublicaNepal_flask.csv",
        parse_dates=['created_at'])
    df_republicanepal['Newspaper'] = "Republica Nepal"

    df_thehimalayan = pd.read_csv(
        "datainnews_v2/static/csvs/thehimalayan_flask.csv",
        parse_dates=['created_at'])
    df_thehimalayan['Newspaper'] = "The Himalayan Times"
    
    
    df_ = df_nepalitimes.append([df_kathmandupost, df_onlinekhabar, df_republicanepal, df_thehimalayan])
    df = df_.groupby('Newspaper').sum().join(df_.groupby('Newspaper').size().to_frame('News Articles'))
    df_month = df_.set_index('created_at').resample('M')['urls'].count().reset_index()
    df_percentage = df_.set_index('created_at').resample('M').sum()
    df_percentage = df_percentage.join(df_month.set_index('created_at'))

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
              {'name': 'Total Articles', 'data': df['Filtered Articles'
              ].tolist()}]
    chart4 = (df['Level 2'] / df['Filtered Articles'] * 100).tolist()

    chart5 = [{'name': 'Level 3', 'data': df['Level 3'].tolist()},
              {'name': 'Total Articles', 'data': df['Filtered Articles'
              ].tolist()}]
    chart6 = (df['Level 3'] / df['Filtered Articles'] * 100).tolist()


    level1 = df[['Newspaper', 'News Articles', 'Level 1', 'Level 1 %']]
    column_names_level1 = level1.columns.values
    row_data_level1 = level1.values.tolist()
    
    level2 = df[['Newspaper', 'News Articles', 'Filtered Articles',
                'Level 2', 'Level 2 %']]
    column_names_level2 = level2.columns.values
    row_data_level2 = level2.values.tolist()

    level3 = df[['Newspaper', 'News Articles', 'Filtered Articles',
                'Level 3', 'Level 3 %']]
    column_names_level3 = level3.columns.values
    row_data_level3 = level3.values.tolist()
    level1_stats = 100*df_percentage['level1_count']/df_percentage['urls']

    newspapers = df['Newspaper'].tolist()
    filtered_articles = round(100*df_percentage['level_2_3_valid'].sum()/df_percentage['urls'].sum(),2)
    content = {
        'pie_filtered_articles': df['Filtered Articles'].sum(),
        'pie_non_filtered_articles': df['News Articles'].sum() - df['Filtered Articles'].sum(),
        'filtered_articles': filtered_articles,
        'level_1_average': round(level1_stats.mean(), 2),
        'level_1_min': round(level1_stats.min(),2),
        'level_1_max': round(level1_stats.max(),2),
        'total_articles': df['News Articles'].sum(),
        'max_date': df_.created_at.max().strftime('%d %b %Y'),
        'newspapers':newspapers,
        'chart0_x': df_month['created_at'].dt.strftime('%b, %Y').tolist(),
        'chart0_y': df_month['urls'].tolist(),
        'chart1_y': (level1_stats).tolist(),
        'chart2_y': (100*df_percentage['level2_count']/df_percentage['level_2_3_valid']).tolist(),
        'chart3_y': (100*df_percentage['level3_count']/df_percentage['level_2_3_valid']).tolist(),
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