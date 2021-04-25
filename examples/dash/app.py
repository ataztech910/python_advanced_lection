#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Dash в себе несет Flask и Pandas

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def hello_world():
    return 'Hello, World!'

df = pd.DataFrame({
    "Фрукты": ["Яблоки", "Апельсины", "Бананы", "Яблоки", "Апельсины", "Бананы"],
    "Количество": [4, 1, 2, 2, 4, 5],
    "Город": ["Вена", "Вена", "Вена", "Линц", "Линц", "Линц"]
})

fig = px.bar(df, x="Фрукты", y="Количество", color="Город", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Наш перый дашборд'),

    html.Div(children='''
        Dash: Фрэймворк для Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)