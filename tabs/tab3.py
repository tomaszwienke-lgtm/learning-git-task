from dash import html, dcc

def render_tab(df):
    return html.Div([
        html.H1('Kanały sprzedaży', style={'text-align': 'center'}),
        html.Div([
            dcc.DatePickerRange(
                id='sales-range-tab3',
                start_date=df['tran_date'].min(),
                end_date=df['tran_date'].max(),
                display_format='YYYY-MM-DD'
            )
        ], style={'width': '100%', 'text-align': 'center', 'margin': '20px'}),
        dcc.Graph(id='weekly-sales-chart'),
        html.H3('Podsumowanie kanałów sprzedaży'),
        html.Div(id='channel-summary-table')
    ])