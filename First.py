import dash


import plotly.graph_objs as go

import dash_core_components as dcc

import dash_html_components as html
from dash import Input, Output

import numpy as np
import pandas as pd
import plotly.express as px

external_stylesheet = [
    {
    'href':"https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css",
    'rel':"stylesheet",
    'integrity': "sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC",
    'crossorigin':"anonymous"
}
]
first = pd.read_csv('C:\\Users\\DELL\\Downloads\\state_wise_daily data file IHHPET.csv')
total = first.shape[0]
confirmed = first[first['Status']=='Confirmed'].shape[0]
recovered = first[first['Status']=='Recovered'].shape[0]
Deceased = first[first['Status']=='Deceased'].shape[0]
option = [
    {'label':'All', 'value':'All'},
    {'label':'Hospitalized', 'value':'Hospitalized'},
    {'label':'Recovered', 'value':'Recovered'},
    {'label':'Deceased', 'value':'Deceased'}
]

option1 = [
    {'label':'All', 'value':'All'},
    {'label':'Mask', 'value':'Mask'},
    {'label':'Sanitizer', 'value':'Sanitizer'},
    {'label':'Oxygen', 'value':'Oxygen'}
]

option2 = [
    {'label':'Red Zone', 'value':'Red Zone'},
    {'label':'Blue Zone', 'value':'Blue Zone'},
    {'label':'Green Zone', 'value':'Green Zone'},
    {'label':'Orange Zone', 'value':'Orange Zone'}
]
app = dash.Dash(__name__,external_stylesheets=external_stylesheet)


app.layout = html.Div([
    html.H1('Corona Virus DashBoard', style={ 'text-align': 'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Total Cases'),
                    html.H4(total)
                ], className='card body')
            ], className='card bg-danger')
        ], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Active Cases'),
                    html.H4(confirmed)
                ], className='card body')
            ], className='card bg-info')
        ], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Recovered Cases'),
                    html.H4(recovered)
                ], className='card body')
            ], className='card bg-succes')
        ], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Deceased Cases'),
                    html.H4(Deceased)
                ], className='card body')
            ], className='card bg-warning')
        ], className='col-md-3')
    ], className='row'),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id = 'plot-graph', options= option1, value= 'All'),
                    dcc.Graph(id = 'graph')
                ], className= 'card body')
            ], className= 'card, bg-warning')
        ], className= 'col-md-6' ),
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id = 'my_dropdown', options= option2, value= 'Status'),
                    dcc.Graph('the_graph')
                ], className='card body')
            ], className= 'card bg-info')
        ], className= 'col-md-6')
    ], className='row'),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        dcc.Dropdown(id = 'picker', options = option, value = 'All'),
                        dcc.Graph(id = 'bar')
                    ], className= 'card-body')
                ], className= 'card bg-danger' )
            ])
        ], className= 'col_md_12')
    ], className='row')
], className='Container')

@app.callback(Output('bar', 'figure'),[Input('picker', 'value')])


def update_graph(type):
    if type == 'All':
        return {'data': [go.Bar(x = first['State'], y = first['Total'])],
                'layout': go.Layout(title= 'States wise Cases', plot_bgcolor= 'orange')
                }
    if type == 'Hospitalized':
        return {'data': [go.Bar(x = first['State'], y = first['Hospitalized'])],
                'layout': go.Layout(title= 'States wise Cases', plot_bgcolor= 'orange')
                }
    if type == 'Recovered':
        return {'data': [go.Bar(x = first['State'], y = first['Recovered'])],
                'layout': go.Layout(title= 'States wise Cases', plot_bgcolor= 'orange')
                }
    if type == 'Deceased':
        return {'data': [go.Bar(x = first['State'], y = first['Deceased'])],
                'layout': go.Layout(title= 'States wise Cases', plot_bgcolor= 'orange')
                }



@app.callback(Output('graph', 'figure'),[Input('plot-graph', 'value')])
def generate_graph(type):
    if type == 'All':
        return {'data': [go.Line(x = first['Status'], y = first['Total'])],
                'layout': go.Layout(title= 'Commodities Total Count', plot_bgcolor= 'green')
                }
    if type == 'Mask':
        return {'data': [go.Line(x=first['Status'], y=first['Mask'])],
                'layout': go.Layout(title='Commodities Total Count', plot_bgcolor='green')
                }
    if type == 'Sanitizer':
        return {'data': [go.Line(x=first['Status'], y=first['Sanitizer'])],
                'layout': go.Layout(title='Commodities Total Count', plot_bgcolor='green')
                }
    if type == 'Oxygen':
        return {'data': [go.Line(x=first['Status'], y=first['Oxygen'])],
                'layout': go.Layout(title='Commodities Total Count', plot_bgcolor='green')
                }



@app.callback(Output('the_graph', 'figure'),[Input('my_dropdown', 'value')])
def pie_graph(my_dropdown):
    piechart = px.pie(data_frame = first, names= my_dropdown, hole = 0.3)
    return piechart


if __name__ == '__main__':
    app.run_server(debug = True)


