import numpy as np
import datetime as dt
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(children=[
    html.Div(children='''Hier ist die Ueberschrift!!!'''),
    dcc.Interval(
            id='interval_component',
            interval=10000,
            n_intervals=0
            ),
    html.Div(id='output-graph')
])


# Funktion zum Auslesen des Datenfiles
def read_from_file():
    datey = lambda x: dt.datetime.strptime(x,'%d.%m.%Y_%H:%M:%S')
    D = np.loadtxt('/media/web/thermometer/temp.dat',delimiter=" ",usecols=[0],
                dtype=dt.datetime,converters={0:datey})
    Z = np.loadtxt('/media/web/thermometer/temp.dat',delimiter=" ",usecols=[1])
    return D, Z


@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input('interval_component', 'n_intervals')])
def update_value(input_data):
    xdata, ydata = read_from_file()
    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': xdata, 'y': ydata, 'type': 'line', 'name': input_data},
            ]
        }
    )

if __name__ == '__main__':
    app.run_server(debug=True)

