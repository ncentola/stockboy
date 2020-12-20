import dash
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from utils import get_product_quantities

data = get_product_quantities()

app = dash.Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(
        id='datatable-interactivity',
        style_table={
            'whiteSpace': 'normal',
            'height': 'auto',
            'lineHeight': '100px',
            'fontSize': 20,
            'width': 'auto'
        },
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": True} for i in pd.DataFrame(data).columns
        ],
        data=data,
        editable=False,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 100,
    ),
    html.Div(id='datatable-interactivity-container'),
    dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=1000000000
        )
])

@app.callback(Output('datatable-interactivity', 'data'), [Input('interval-component', 'n_intervals')])
def refresh_data(n):
    # global data
    data = get_product_quantities()
    return data

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
