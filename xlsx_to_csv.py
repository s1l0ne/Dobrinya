import pandas as pd
import os


for folder in os.listdir('./rgd'):
    input_files = os.listdir(f'./rgd/{folder}')

    for input_file in input_files:
        path_xlsx = f'./rgd/{folder}/{input_file}'
        path_csv = f'./csv/{folder}/{input_file.split('.')[0]}.csv'

        try:
            pd.read_excel(path_xlsx).to_csv(path_csv, index=False)
            print(input_file)
        except:
            print(f'Some problem with {path_xlsx}')