import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
from dash import Input, Output
from dash import State
import numpy as np
import scipy as scp



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

efficiency_samples_m = pd.read_csv('efficiency_m.csv')
efficiency_samples_w = pd.read_csv('efficiency_w.csv')
samples_df = pd.concat([efficiency_samples_m, efficiency_samples_w], axis=1)


app.layout = html.Div([
    
    html.Div([
        html.Label('Select your athletes', style={'font-size':18, 'margin-bottom':-30}),
        html.Hr(),
        html.Label('For a clearer plot we suggest not to choose more than 4-5 competitors at a time', style={'margin-top':'-30px', 'font-size':10}),
        dcc.Dropdown(all_names,
                     all_names[0],
                     multi=True, style={ 'width':'1000px','height':'37px', 'margin-bottom':'50px'},
                    id = 'athlete_selection', searchable=False, placeholder='Select your athletes'
                    ),
        html.Hr(),
    ]),
    dcc.Graph(id='athlete_efficiency', style={'margin-top':'50px', 'margin-bottom':'10px', 'width': '180vh', 'height': '90vh'})  
    
    
    
    
], style={'padding': 1, 'flex': 1})


@app.callback(
    Output('athlete_efficiency', 'figure'),
    Input('athlete_selection', 'value'))
def update_graph(athletes):
    fig = px.histogram(samples_df, x=athletes, histnorm='probability density')
    fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    fig.update_layout(
    xaxis_title="Efficiency", yaxis_title="Normalized counts", legend_title='Legend', title='Efficiency of the top biathletes', title_font_size=25)
    fig.update_xaxes(ticks="outside", showline=True, linecolor='black', linewidth=2)
    fig.update_yaxes(ticks="outside", showline=True, linecolor='black', linewidth=2)
    fig.update_traces(marker_line_width=1,marker_line_color="white")
    

    return fig



    


if __name__ == '__main__':
    app.run_server(debug=True)
