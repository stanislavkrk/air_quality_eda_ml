import os
import pandas as pd

def loader(dir_one='data', dir_two='raw', file_name='AirQualityUCI.csv'):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    temp_path = os.path.join(current_dir, '..', dir_one, dir_two, file_name)
    data = os.path.abspath(temp_path)
    df = pd.read_csv(data, sep=';')
    return df

def drop_empty_rows(df):
    print('Initial shape: ' + str(df.shape))
    print(df[df['Date'].isnull()])
    df.dropna(how='all', inplace=True)
    print('Result shape: ' + str(df.shape))