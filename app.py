from components.input import create_input
from themes import *
import pandas as pd
from dash import Dash, State, Output, Input, html, dcc, callback


def booststrap():
    port = "8080"

    app = Dash(name="Dashboard", url_base_pathname="/dashboard/")
    app.layout = html.Div([html.H1("Hello world"), create_input()])

    if __name__ == "__main__":
        app.run(debug=True, port=port)


booststrap()
