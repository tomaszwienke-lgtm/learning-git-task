import pandas as pd
import os

def load_and_clean_data():
    # Wczytaj transakcje
    src = 'db/transactions'
    transactions = pd.DataFrame()
    for filename in os.listdir(src):
        if filename.endswith('.csv'):
            file_path = os.path.join(src, filename)
            df_part = pd.read_csv(file_path, index_col=0, parse_dates=['tran_date'], dayfirst=True)
            transactions = pd.concat([transactions, df_part], ignore_index=True)

    # Wczytaj pozostałe pliki
    customers = pd.read_csv('db/customers.csv', index_col=0)
    prod_info = pd.read_csv('db/prod_cat_info.csv')
    cc = pd.read_csv('db/country_codes.csv', index_col=0)

    # Dołącz kategorie
    prod_cat_unique = prod_info.drop_duplicates(subset=['prod_cat_code']).set_index('prod_cat_code')['prod_cat']
    df = transactions.join(prod_cat_unique, on='prod_cat_code', how='left')
    prod_subcat_unique = prod_info.drop_duplicates(subset=['prod_sub_cat_code']).set_index('prod_sub_cat_code')['prod_subcat']
    df = df.join(prod_subcat_unique, on='prod_subcat_code', how='left')

    # Dołącz klientów i kraje
    customers_with_country = customers.join(cc, on='country_code', how='left')
    customers_with_country = customers_with_country.set_index('customer_Id')
    df = df.join(customers_with_country, on='cust_id', how='left')

    # Czyszczenie
    df['tran_date'] = pd.to_datetime(df['tran_date'], dayfirst=True, errors='coerce')
    df = df.dropna(subset=['tran_date'])
    df = df.drop_duplicates(subset=['transaction_id'], keep='first')
    df['month_year'] = df['tran_date'].dt.to_period('M').astype(str)

    return df