# external_stylesheets = ['C:/Users/Sikandar Hayat/Desktop\Social_ecnomic/assests/external.css']
from dash import Dash, dcc, html, callback, Input, Output

external_stylesheets = ['C:/Users/Sikandar Hayat/Desktop/Social_ecnomic/assests/external.css']
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    # represents the browser address bar and doesn't render anything
    dcc.Location(id='url', refresh=False),

    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Navigate to "/page-2"', href='/page-2'),

    # content will be rendered in this element
    html.Div(id='page-content')
])


@callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    return html.Div([
        html.H3(f'You are on page {pathname}')
    ])


if __name__ == '__main__':
    app.run_server(debug=True)