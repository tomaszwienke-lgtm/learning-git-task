import plotly.express as px
import plotly.graph_objects as go
from dash import html
import pandas as pd

def create_weekly_chart(filtered_df):
    filtered_df = filtered_df.copy()
    filtered_df['weekday'] = filtered_df['tran_date'].dt.day_name()
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekly = filtered_df.groupby(['weekday', 'Store_type'])['total_amt'].sum().reset_index()
    weekly['weekday'] = pd.Categorical(weekly['weekday'], categories=weekday_order, ordered=True)
    weekly = weekly.sort_values('weekday')
    fig = px.bar(weekly, x='weekday', y='total_amt', color='Store_type',
                 title='Przychody w dniach tygodnia według kanału sprzedaży',
                 labels={'total_amt': 'Przychód', 'weekday': 'Dzień tygodnia'})
    return fig

def create_channel_summary(filtered_df):
    summary = filtered_df.groupby('Store_type').agg(
        Liczba_transakcji=('transaction_id', 'count'),
        Liczba_klientów=('cust_id', 'nunique'),
        Średnia_wartość=('total_amt', 'mean')
    ).reset_index()
    gender_counts = filtered_df.dropna(subset=['Gender']).groupby(['Store_type', 'Gender']).size().reset_index(name='count')
    gender_counts = gender_counts.sort_values(['Store_type', 'count'], ascending=[True, False])
    gender_counts = gender_counts.drop_duplicates(subset='Store_type')
    summary = summary.merge(gender_counts[['Store_type', 'Gender']], on='Store_type', how='left')
    summary.rename(columns={'Gender': 'Dominująca płeć'}, inplace=True)
    summary['Średnia_wartość'] = summary['Średnia_wartość'].round(2)

    table_header = [html.Tr([html.Th(col) for col in summary.columns])]
    table_rows = [html.Tr([html.Td(summary.iloc[i][col]) for col in summary.columns]) for i in range(len(summary))]
    return html.Table(table_header + table_rows, style={'width': '100%', 'border': '1px solid black', 'margin-top': '20px'})