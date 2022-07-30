from turtle import color
from dash import Dash ,html, dcc,Input,Output
import dash_bootstrap_components as dbc   
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from alpha_vantage.timeseries import TimeSeries # pip install alpha-vantage
import datetime as dt

external_stylesheets = ['external.css']
# Load the Data
Data=pd.read_csv('C:/Users/Sikandar Hayat/Desktop/Social_ecnomic/Data.csv')
List=Data['country'].values.tolist()

colors = {
    'background': 'white',
    'text': '#7FDBFF'
}

app = Dash(__name__, external_stylesheets=external_stylesheets)



app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Socioeconomic Dashboard',
        style={
            'textAlign': 'center',
            'color': 'red'
        }
    ),

    html.Div(children='Dash: A web application framework for your data.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.Br(),
    
    html.Div(children='Population of the country', style={
        # 'textAlign': 'center',
        'font-size': 30,
        'color': 'Blue'
    }),
     html.Br(),
     html.Div([
        html.Label(['Select the country    Name']),
        dcc.Dropdown(
            id='my_dropdown',
            options=List,
            value='Pakistan',
            placeholder="Select a Country",
            # multi=False,

            style = {'width': '41%',  'align-items': 'center', 'justify-content': 'center'}
        ),
    ]),


    html.Div([
        html.H1(
        children='Total Population of the country is',
        style={
            'color': 'blue',
            'font-size': 30,
            
        }
    ),
        dcc.Graph(id='the_graph' )
    ],style = {'width': '30%',"border":"2px black solid"}),


])

@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)

def update_graph(my_dropdown):
    dff = Data[Data['country']==my_dropdown]
    
    V1=dff['Population_female'].sum()
    V2=dff['Population_male'].sum()
    fig = go.Figure(data=[go.Pie(labels=['male','Female'], values=[V1,V2], hole=.4,title=my_dropdown)])
    

    
    return (fig)
    update_graph


    
    
    

if __name__ == '__main__':
    app.run_server(debug=True)