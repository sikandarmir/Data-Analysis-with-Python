from turtle import color
from dash import Dash ,html, dcc,Input,Output
import dash_bootstrap_components as dbc   
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from alpha_vantage.timeseries import TimeSeries # pip install alpha-vantage
import datetime as dt
import numpy as np
from plotly.subplots import make_subplots

external_stylesheets = ['C:/Users/Sikandar Hayat/Desktop/Social_ecnomic/assests/external.css']
# Load the Data
Data=pd.read_csv('C:/Users/Sikandar Hayat/Desktop/Social_ecnomic/Data.csv')
List=Data['Region'].unique()
#Population
Data_1=pd.read_csv('C:/Users/Sikandar Hayat/Desktop/Social_ecnomic/Data.csv')
List_1=Data['country'].values.tolist()

colors = {
    'background': 'white',
    'text': '#7FDBFF'
}

app = Dash(__name__, external_stylesheets=external_stylesheets)



app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Social Economic Dashboard',
        style={
            'textAlign': 'center',
            'color': 'red'
        }
    ),
    html.Div(children='Dash: A web application framework for Scoial Ecnomic data in all over the world.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.Br(),
    
    html.Div(children='GDP: Gross domestic product (million current US$) & GDP per capita (current US$)', style={
        # 'textAlign': 'center',
        'font-size': 30,
        'color': 'Blue'
    }),

     html.Br(),
     html.Div([
        html.Label(['Select the Region']),
        dcc.Dropdown(
            id='my_dropdown',
            options=List,
            value='EasternEurope',
            placeholder="Select a Country",
            # multi=False,

            style = {'width': '200px',  'align-items': 'center', 'justify-content': 'center','background': '#7FDBFF',}
        ),
    ]),


    html.Table([
   html.Tr([

            html.Td([
                 html.Div([
        html.H1(
        children='GDP of the different countries in selected Region',
        style={
            'color': 'blue',
            'font-size': 30,
            'padding-left:' :'50px'
            
        }
    ),
    ###Graph function
        dcc.Graph(id='the_graph' )
    ],style = {'width': '750px',"border":"2px black solid"}),
            ]),


        html.Td([
            html.Div([
        html.H1(
        children='GDP of the selected Region',
        style={
            'color': 'blue',
            'font-size': 30,
            'right':50,
            
        }
    ),
    ###Graph function
        dcc.Graph(id='the_graph_1' )
    ],style = {'width': '550px',"border":"2px black solid"}),

        ]),

   ]), #Last of row

        
        
        
        
        ]),#  //Last of table



        html.Br(),
        html.Br(),

        
 html.Div(children='Population of the Differnt Countries in all over the world', style={
        'textAlign': 'center',
        'font-size': 30,
        'color': 'Blue'
    }),
    
    html.Br(),
    html.Br(),

html.Table([
    html.Tr([
    html.Td([
            
    #Population country  Drop down
     html.Div([
        html.Label(['Select the country Name']),
        dcc.Dropdown(
            id='my_dropdown_1',
            options=List_1,
            value='Pakistan',
            placeholder="Select a Country",
            # multi=False,

            style = {'width': '200px',  'align-items': 'center', 'justify-content': 'center','background': '#7FDBFF'}
        ),
    ]),


# Population of the country  Graph
    html.Div([
        html.H1(
        children='Male and Female Ratio of the Selected Country',
        style={
            'color': 'blue',
            'font-size': 30,
            
        }
    ),
        dcc.Graph(id='the_graph_2' )
    ],style = {'width': '500px',"border":"2px black solid"}),


    ]), #colunm 1 end
     html.Td([
     html.Div([
        html.Label(['Select the Region']),
        dcc.Dropdown(
            id='my_dropdown_2',
            options=List,
            value='WesternEurope',
            placeholder="Select a region",
            # multi=False,

            # style = {'width': '200px',  'align-items': 'center', 'justify-content': 'center','background': 'grey',}
            style = {'width': '200px',  'align-items': 'center', 'justify-content': 'center','background': '#7FDBFF'}
        ),
    ]),
    #Graph of Population  Region
    # Population of the country  Graph
    html.Div([
        html.H1(
        children='Population of Different countries in the Selected Region ',
        style={
            'color': 'blue',
            'font-size': 30,
            
        }
    ),
        dcc.Graph(id='the_graph_3' )
    ],style = {'width': '800px',"border":"2px black solid"}),


     ]),#colunm 2 end

    ]),#Row End
]),#Table End




        html.Br(),
        html.Br(),

        
 html.Div(children='Life Expentency  of the Differnt Countries in all over the world', style={
        'textAlign': 'center',
        'font-size': 30,
        'color': 'Blue'
    }),
    
    html.Br(),
    html.Br(),

#Life Expectancy Graph
html.Table([

    html.Tr([

        html.Td([
             html.Div([
        html.Label(['Select the country Name']),
        dcc.Dropdown(
            id='my_dropdown_3',
            options=List_1,
            value='Pakistan',
            placeholder="Select a Country",
            # multi=False,

            style = {'width': '200px',  'align-items': 'center', 'justify-content': 'center','background': '#7FDBFF'}
        ),
    ]),
    
    # Life Expectancy of the country  Graph
    html.Div([
        html.H1(
        children='Life Expectancy of the Selected Country ',
        style={
            'color': 'blue',
            'font-size': 30,
            
        }
    ),
        dcc.Graph(id='the_graph_4' )
    ],style = {'width': '500px',"border":"2px black solid"}),

]),#End of colunm

#Start
# Life Expectancy in selected Region
html.Td([
     html.Div([
        html.Label(['Select the Region']),
        dcc.Dropdown(
            id='my_dropdown_4',
            options=List,
            value='WesternEurope',
            placeholder="Select a region",
            # multi=False,

            # style = {'width': '200px',  'align-items': 'center', 'justify-content': 'center','background': 'grey',}
            style = {'width': '200px',  'align-items': 'center', 'justify-content': 'center','background': '#7FDBFF'}
        ),
    ]),
    #Graph of Population  Region
    # Population of the country  Graph
    html.Div([
        html.H1(
        children='Population of Different countries in the Selected Region ',
        style={
            'color': 'blue',
            'font-size': 30,
            
        }
    ),
        dcc.Graph(id='the_graph_5' )
    ],style = {'width': '800px',"border":"2px black solid"}),


     ]),#colunm 2 end




    ]),#End of Row
]),#End of Table)


])

@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    Output(component_id='the_graph_1', component_property='figure'),
    Output(component_id='the_graph_2', component_property='figure'),
    Output(component_id='the_graph_3', component_property='figure'),
    Output(component_id='the_graph_4', component_property='figure'),
    Output(component_id='the_graph_5', component_property='figure'),


    


    [Input(component_id='my_dropdown', component_property='value'),
    Input(component_id='my_dropdown_1', component_property='value'),
    Input(component_id='my_dropdown_2', component_property='value'),
    Input(component_id='my_dropdown_3', component_property='value'),
    Input(component_id='my_dropdown_4', component_property='value')



    
    


    ]
    
    
    
)


def update_graph(my_dropdown,my_dropdown_1,my_dropdown_2,my_dropdown_3,my_dropdown_4):

    County_list=Data[Data['Region']==my_dropdown]['country'].to_list()
# lis
    total_GDP=Data[Data['Region']==my_dropdown]['GDP: Gross domestic product (million current US$)'].to_list()
# total_pop
    GDP_per_Cap=Data[Data['Region']==my_dropdown]['GDP per capita (current US$)'].to_list()
    # male_pop




    y_saving = total_GDP

    y_net_worth=GDP_per_Cap
    # x = ['Japan', 'United Kingdom', 'Canada', 'Netherlands',
    #      'United States', 'Belgium', 'Sweden', 'Switzerland']
    x=County_list


    # Creating two subplots
    fig = make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=True,
                        shared_yaxes=False, vertical_spacing=0.001)

    fig.append_trace(go.Bar(
        x=y_saving,
        y=x,
        marker=dict(
            color='rgba(50, 171, 96, 0.6)',
            line=dict(
                color='rgba(50, 171, 96, 1.0)',
                width=1),
        ),
        name='GDP: Gross domestic product (million current US$)',
        orientation='h',
    ), 1, 1)

    fig.append_trace(go.Scatter(
        x=y_net_worth, y=x,
        mode='lines+markers',
        line_color='rgb(128, 0, 128)',
        name='GDP per capita (current US$)',
    ), 1, 2)

    fig.update_layout(
        title='GDP: Gross domestic product (million current US$) & GDP per capita',
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=True,
            domain=[0, 0.85],
        ),
        yaxis2=dict(
            showgrid=False,
            showline=True,
            showticklabels=False,
            linecolor='rgba(102, 102, 102, 0.8)',
            linewidth=2,
            domain=[0, 0.85],
        ),
        xaxis=dict(
            zeroline=False,
            showline=False,
            showticklabels=True,
            showgrid=True,
            domain=[0, 0.42],
        ),
        xaxis2=dict(
            zeroline=False,
            showline=False,
            showticklabels=True,
            showgrid=True,
            domain=[0.47, 1],
            side='top',
            dtick=25000,
        ),
        legend=dict(x=0.029, y=1.038, font_size=10),
        margin=dict(l=100, r=20, t=70, b=70),
        paper_bgcolor='rgb(248, 248, 255)',
        plot_bgcolor='rgb(248, 248, 255)',
    )

    annotations = []

    y_s = np.round(y_saving, decimals=2)
    y_nw = np.rint(y_net_worth)

    # Adding labels
    for ydn, yd, xd in zip(y_nw, y_s, x):
        # labeling the scatter savings
        annotations.append(dict(xref='x2', yref='y2',
                                y=xd, x=ydn,
                                text='{:,}'.format(ydn) + 'K',
                                font=dict(family='Arial', size=12,
                                        color='rgb(128, 0, 128)'),
                                showarrow=False))
        # labeling the bar net worth
        annotations.append(dict(xref='x1', yref='y1',
                                y=xd, x=yd + 3,

                                text=str(yd),
                                font=dict(family='Arial', size=12,
                                        color='rgb(50, 171, 96)'),
                                showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper',
                            x=-0.2, y=-0.109,
                            text='OECD "' +
                                'GDP: Gross domestic product (million current US$) & GDP per capita'+
                                '10.1787/cfc6f499-en (Accessed on 05 June 2017)',
                            font=dict(family='Arial', size=10, color='rgb(150,150,150)'),
                            showarrow=False))

    fig.update_layout(annotations=annotations)
    
        #Figure 2
    
    country=Data[Data['Region']==my_dropdown]['country'].to_list()
    total_GDP_=Data[Data['Region']==my_dropdown]['GDP: Gross domestic product (million current US$)'].to_list()

        # V1=dff['Population_female'].sum()
        # V2=dff['Population_male'].sum()

    fig1 = go.Figure(data=[go.Pie(labels=country, values=total_GDP, hole=.4,title=my_dropdown)])
    # return fig

    #Population of country Graph

    dff = Data_1[Data_1['country']==my_dropdown_1]
    
    V1=dff['Population_female'].sum()
    V2=dff['Population_male'].sum()
    fig_2 = go.Figure(data=[go.Pie(labels=['male','Female'], values=[V1,V2], hole=.4,title=my_dropdown_1)])
    
    #Population of region graph

    df=Data[Data['Region']==my_dropdown_2]
    fig_3 = px.bar(df, y='Total_Population', x='country', text_auto='.2s',
    title="Population of the Region")
    # fig.show()


    # Life Expectency 
    df=Data[Data['country']==my_dropdown_3]
    Vx1=df['Life_expec_female'].max()
    Vx2=df['Life_expec_male'].max()
    Vx3=df['life_expec_total'].max()
        # import plotly.graph_objects as go
    y=[Vx1, Vx2, Vx3]
    x=['Life_expectancy_female', 'Life_expectance_male', 'Life_expectancy Total',]
# fig = go.Figure([go.Bar(x=animals, y=[V1, V2, V3]),text=y,textposition='auto',])
# fig.show()
    fig5 = go.Figure(data=[go.Bar(
            x=x, y=y,
            text=y,
            textposition='auto',width=[0.4, 0.4, 0.4], 
        )])

    fig5.update_layout(
        yaxis=dict(
        title='Age',
        titlefont_size=16,
        tickfont_size=14,
    ),
     xaxis=dict(
        title='Gender',
        titlefont_size=16,
        tickfont_size=14,
    ),
    height=400, width=500,
    title_text="Life Expectance",
    barmode="stack",
    uniformtext=dict(mode="hide", minsize=10),
    )

# fig.show()

    #Life expectancy of region
    df=Data[Data['Region']==my_dropdown_4]
    fig6 = go.Figure()

# Add traces
    fig6.add_trace(go.Scatter(x=df['country'], y=df['Life_expec_female'],
                    mode='markers',
                    name='Life_expectancy female'))
    fig6.add_trace(go.Scatter(x=df['country'], y=df['Life_expec_male'],
                    mode='lines+markers',
                    name='Life_expectancy male'))
    fig6.add_trace(go.Scatter(x=df['country'], y=df['life_expec_total'],
                    mode='lines',
                    name='Total life expectancy'))
    fig6.update_layout(
    title_text="Life Expectancy of the region"
    )

# Set x-axis title
    fig6.update_xaxes(title_text="Country")
    fig6.update_yaxes(title_text="age")
# fig.show()

    

    
    # return (fig)
    return [fig,fig1,fig_2,fig_3,fig5,fig6]
    
    
# def update_graphd(my_dropdown):
#     country=Data[Data['Region']==my_dropdown]['country'].to_list()
#     total_GDP_=Data[Data['Region']==my_dropdown]['GDP: Gross domestic product (million current US$)'].to_list()

#         # V1=dff['Population_female'].sum()
#         # V2=dff['Population_male'].sum()

#     fig1 = go.Figure(data=[go.Pie(labels=country, values=total_GDP, hole=.4,title=my_dropdown)])
#     return fig2

# fig.show()
    
    
    update_graph
    

if __name__ == '__main__':
    app.run_server(debug=True)