import matplotlib.pyplot as plt
import pandas as pd

def datetime_trend(df):

    df_temp = df.set_index('DateTime').copy()
    df_temp.index = pd.to_datetime(df_temp.index)  # <-- ключовий момент
    df_temp.sort_index(inplace=True)

    df_temp['rolling_1H'] = df_temp['C6H6(GT)'].rolling('1h').mean()
    df_temp['rolling_12H'] = df_temp['C6H6(GT)'].rolling('12h').mean()
    df_temp['rolling_7D'] = df_temp['C6H6(GT)'].rolling('7D').mean()

    plt.figure(figsize=(16, 6))
    plt.plot(df_temp.index, df_temp['rolling_1H'], color='blue', label='1H Rolling Mean')
    plt.plot(df_temp.index, df_temp['rolling_12H'], color='orange', label='12H Rolling Mean')
    plt.plot(df_temp.index, df_temp['rolling_7D'], color='green', label='7D Rolling Mean')
    plt.xlabel('Date and time')
    plt.ylabel('C6H6(GT)')
    plt.title('Smoothed trends')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
