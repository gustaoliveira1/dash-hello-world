import pandas as pd
import plotly.express as px
from dash import Output, Input, callback, dcc, html


def create_input():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
    )

    @callback(
        Output(component_id="output", component_property="figure"),
        Input(component_id="input", component_property="value"),
        prevent_initial_call=True,
    )
    def output(value):
        filter = df.query(f"continent.str.contains('{value}')")
        return px.histogram(filter, x="continent", y="lifeExp", histfunc="avg")

    return html.Div(
        [
            dcc.Input(
                id="input",
            ),
            dcc.Graph(
                figure=px.histogram(df, x="continent", y="lifeExp", histfunc="avg"),
                id="output",
            ),
        ]
    )
