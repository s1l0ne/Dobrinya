import os
import connect


conn = connect.connect()
cur = conn.cursor()

cur.execute('CREATE SCHEMA IF NOT EXISTS rgd')
conn.commit()

columns = ('report_month, report_year, cargo_code, departure_road, '
           'destination_road, departure_station, destination_station, '
           'shipping_category, type, cargo_weight, wagon_count, '
           'container_count, carriage_fee')

for folder in os.listdir('./csv'):
    input_files = os.listdir(f'./csv/{folder}')

    for input_file in input_files:
        file_path = f'./csv/{folder}/{input_file}'
        table_name = input_file.split('.')[0]

        with open(file_path, 'r', encoding='utf-8') as f:
            cur.execute(f'CREATE TABLE IF NOT EXISTS rgd."{table_name}" ({' VARCHAR,'.join(columns.split(', '))} VARCHAR)')
            cur.copy_expert(f'COPY rgd."{table_name}" ({columns}) FROM STDIN WITH CSV HEADER', f)

        conn.commit()
