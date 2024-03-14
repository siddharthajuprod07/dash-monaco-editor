import dash_monaco_editor
from dash import Dash, callback, html, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    dash_monaco_editor.DashMonacoEditor(
        id="input",
        height='90vh',
        language='python',
        value='##some comment',
        theme="vs-dark"
    ),
    html.Div(id='output')
])


@callback(Output('output', 'children'), Input('input', 'value'))
def display_output(value):
    return 'You have entered {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
