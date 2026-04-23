import csv
from sqlalchemy import create_engine, MetaData, Table, Column, String
from sqlalchemy.sql import insert

engine = create_engine('sqlite:///weather.db', echo=True)
meta = MetaData()

def create_table_from_csv(csv_path, table_name):
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
    
    columns = [Column(h, String) for h in headers]
    
    # Jeśli jest kolumna 'id', ustawiamy ją jako klucz główny
    for i, col in enumerate(columns):
        if col.name.lower() == 'id':
            columns[i] = Column(col.name, String, primary_key=True)
            break
    
    return Table(table_name, meta, *columns)

stations = create_table_from_csv('clean_stations.csv', 'stations')
measures = create_table_from_csv('clean_measure.csv', 'measures')

meta.create_all(engine)
print("Tables created.")

def insert_csv(csv_path, table):
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    with engine.connect() as conn:
        conn.execute(insert(table), rows)
        # commit nie jest potrzebny – nastąpi automatycznie
    
    print(f"Inserted {len(rows)} rows into table {table.name}")

insert_csv('clean_stations.csv', stations)
insert_csv('clean_measure.csv', measures)   # uwaga: poprawna nazwa pliku?

print("Database ready!")



