import pandas
from dash import Dash, html, dcc, Input, Output

from plotly.express import line

path = "./formatted_daily_sales_data.csv"
colours = {
    "primary": "#000080",
    "secondary": "#00D5FF",
    "font": "#FFFFFF"
}

data = pandas.read_csv(path)
data = data.sort_values(by="date")

dash_app = Dash(__name__)

def generate_figure(chart_data):
    line_chart = line(chart_data, x="date", y="sales", title="Pink Morsel Sales")
    line_chart.update_layout(
        plot_bgcolor=colours["secondary"],
        paper_bgcolor=colours["primary"],
        font_color=colours["font"],
    )
    return line_chart


visualisation = dcc.Graph(
    id="visualisation",
    figure=generate_figure(data)
)

header = html.H1(
    "Pink Morsel Visualiser",
    id="header",
    style={
        "background-color": colours["secondary"],
        "color": colours["font"],
        "border-radius": "20px",
        "font-family": "Arial"
    }
)

region_picker = dcc.RadioItems(
    ["north", "east", "south", "west", "all"],
    "north",
    id="region_picker",
    inline=True
)
region_picker_wrapper = html.Div(
    [
        region_picker
    ],
    style={
        "font-size": "150%",
        "color": colours["font"],
        "font-family": "Arial"
    }
)

@dash_app.callback(
    Output(visualisation, "figure"),
    Input(region_picker, "value")
)
def update_graph(region):
    if region == "all":
        trimmed_data = data
    else:
        trimmed_data = data[data["region"] == region]

    figure = generate_figure(trimmed_data)
    return figure

dash_app.layout = html.Div(
    [
        header,
        visualisation,
        region_picker_wrapper
    ],
    style={
        "textAlign": "center",
        "background-color": colours["primary"],
        "border-radius": "20px",
        "font-family": "Arial"
    }
)

if __name__ == '__main__':
    dash_app.run_server()