import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
from datetime import datetime as dt


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1("Componentes principales"),
    html.Div(children = [
        html.H3("Dropdown:"),
        dcc.Dropdown(
            options=[
                {'label': 'Paris', 'value': 'Paris'},
                {'label': 'Roma', 'value': 'Roma'},
                {'label': 'Berlin', 'value': 'Berlin'}
            ],
            value='Paris'
        ),
        
        html.Br(),
        html.H3("Slider:"),
        dcc.Slider(
            min=-5,
            max=5,
            marks={int(i): 'Label {}'.format(i) for i in np.arange(-5,6)},
            value=5,
        ), 

        html.Br(),
        html.H3("RangeSlider:"),
        dcc.RangeSlider(
            marks={int(i): 'Label {}'.format(i) for i in np.arange(-5, 6)},
            min=-5,
            max=5,
            value=[-2,2]
        ),

        html.Br(),
        html.H3("Input: Existen muchos tipos"),
        dcc.Input(
            placeholder='Introduce tu contraseña...',
            type='password',
            value=''
        ),

        html.Br(),
        html.H3("TextArea:"),
        dcc.Textarea(
            placeholder='Escribe sobre ti',
            value='',
            style={'width': '100%'}
        ),

        html.Br(),
        html.H3("Checkboxes:"),
        dcc.Checklist(
            options=[
                {'label': 'Paris', 'value': 'Paris'},
                {'label': 'Roma', 'value': 'Roma'},
                {'label': 'Berlin', 'value': 'Berlin'}
            ],
            value=['Paris']
        ),

        html.Br(),
        html.H3("Radio Items:"),
        dcc.RadioItems(
            options=[
                {'label': 'Paris', 'value': 'Paris'},
                {'label': 'Roma', 'value': 'Roma'},
                {'label': 'Berlin', 'value': 'Berlin'}
            ],
            value='Paris'
        ),

        html.Br(),
        html.H3("Button:"),
        html.Button('Enviar', id='button'),

        html.Br(),
        html.H3("Dates:"),

        dcc.DatePickerSingle(
            id='date-picker-single',
            placeholder="Fecha ida"
        ),

        dcc.DatePickerRange(
            id='date-picker-range',
            start_date=dt(2019, 5, 10),
            end_date_placeholder_text = "Fecha vuelta"
        ),

        html.Br(),
        html.H3("Markdown:"),
        dcc.Markdown('''
            *Escribo en cursiva* y en **negrita**.
            #### Titulo 4

            [Enlace](https://dash.plot.ly/dash-core-components).
        '''),

        html.Br(),
        html.H3("Upload:"),
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Arrastra o ',
                html.A('Selecciona ficheros')
            ])
        ),

        html.Br(),
        html.H3("Pestañas:"),
        dcc.Tabs(id="pests", value='pest-1', children=[
            dcc.Tab(label='Pestaña 1', value='pest-1', children = [html.Div("Hello tab!")]),
            dcc.Tab(label='Pestaña 2', value='pest-2'),
        ]),

        html.Br(),
        html.H3("Graficos:"),
        dcc.Graph(
            id='my_first_graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [13, 3, 10], 'type': 'line', 'name': 'line'},
                    {'x': [1, 2, 3], 'y': [4, 10, 2], 'type': 'bar', 'name': 'bar'},
                ],
                'layout': {
                    'title': 'Grafico'
                }
            }
        ),


    ], className = "ten columns")
])

if __name__ == "__main__":
    app.run_server(debug=True)