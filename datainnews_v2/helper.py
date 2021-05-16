import pandas as pd
import plotly.graph_objects as go
import plotly


def get_data_collection_timeline_chart(df_):
    df_month = df_.set_index('created_at').resample('M')['urls'].count().reset_index()
    layout = go.Layout(
        xaxis=dict(
            title="Date"
        ),
        yaxis=dict(
            title="Number of articles collected"
        ) ) 
    fig = go.Figure([go.Scatter(x=df_month['created_at'], y=df_month['urls'])], layout=layout)
    div = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
    return div
