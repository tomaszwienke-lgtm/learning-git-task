import dash
from dash import dcc, html, Input, Output, callback
from modules.data_loader import load_and_clean_data
from tabs import tab3
from modules.charts import create_weekly_chart, create_channel_summary

df = load_and_clean_data()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        dcc.Tabs(id='tabs', value='tab-3', children=[
            dcc.Tab(label='Kanały sprzedaży', value='tab-3')
        ]),
        html.Div(id='channels-container', children=tab3.render_tab(df), style={'display': 'block'})
    ], style={'width': '80%', 'margin': 'auto'})
], style={'height': '100%'})

@callback(
    Output('weekly-sales-chart', 'figure'),
    Input('sales-range-tab3', 'start_date'),
    Input('sales-range-tab3', 'end_date')
)
def update_weekly_chart(start_date, end_date):
    mask = (df['tran_date'] >= start_date) & (df['tran_date'] <= end_date)
    filtered = df.loc[mask]
    return create_weekly_chart(filtered)

@callback(
    Output('channel-summary-table', 'children'),
    Input('sales-range-tab3', 'start_date'),
    Input('sales-range-tab3', 'end_date')
)
def update_summary(start_date, end_date):
    mask = (df['tran_date'] >= start_date) & (df['tran_date'] <= end_date)
    filtered = df.loc[mask]
    return create_channel_summary(filtered)

if __name__ == '__main__':
    app.run(debug=True)