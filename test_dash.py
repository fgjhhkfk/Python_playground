# import pandas_datareader.data as web
import numpy as np
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(children=[
    html.Div(children='''wasauchimmer:'''),
        # dcc.Interval(
        #     id='interval_component',
        #     interval=50000,
        #     n_intervals=0
        #     )
        html.Div(id='output-graph'),

    # html.Div(children='''Symbol to graph:'''),
    #     # dcc.Interval(
    #     #     id='interval_component',
    #     #     interval=50000,
    #     #     n_intervals=0
    #     #     )
    #     html.Button('Click Me', id='my-button'),

])

# Funktio zum auslesen des Datenfiles
def read_from_file():
    data = np.loadtxt('/home/hjk/test.md')
    xdata = data[:,0]
    ydata = data[:,1]
    return xdata, ydata


@app.callback(
    Output(component_id='output-graph', component_property='children'),
    # [Input('interval_component', 'n_intervals')]
    [Input('my-button', 'n_clicks')]
)
def update_value(input_data):
    xdata, ydata = read_from_file()
    print(xdata)
    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': xdata, 'y': ydata, 'type': 'bar', 'name': input_data},
            ],
            # 'layout': {
            #     'title': input_data
            # }
        }
    )

if __name__ == '__main__':
    app.run_server(debug=True)

