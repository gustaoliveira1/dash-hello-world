from dash import Output, Input, callback

first_theme = {"color": "white", "backgroundColor": "blue"}
second_theme = {"color": "white", "backgroundColor": "red"}


@callback(
    Output(component_id="output", component_property="style"),
    Input(component_id="button", component_property="n_clicks"),
)
def change_theme(value):
    click_is_oven = value % 2 == 0
    return first_theme if click_is_oven else second_theme
