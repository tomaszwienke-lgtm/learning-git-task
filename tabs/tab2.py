from dash import html, dcc

def render_tab(df):
    categories = df['prod_cat'].dropna().unique()
    default_category = categories[0] if len(categories) > 0 else None

    return html.Div([
        html.H1('Produkty', style={'text-align': 'center'}),
        html.Div([
            html.Label("Wybierz kategorię produktu:"),
            dcc.Dropdown(
                id='category-dropdown',
                options=[{'label': cat, 'value': cat} for cat in categories],
                value=default_category
            )
        ], style={'margin': '20px'}),
        html.Div([
            html.Label("Zakres dat:"),
            dcc.DatePickerRange(
                id='products-range',
                start_date=df['tran_date'].min(),
                end_date=df['tran_date'].max(),
                display_format='YYYY-MM-DD'
            )
        ], style={'margin': '20px'}),
        html.Div([
            html.Div([dcc.Graph(id='category-pie')], style={'width': '50%'}),
            html.Div([dcc.Graph(id='gender-bar')], style={'width': '50%'})
        ], style={'display': 'flex'})
    ])