from sklearn.preprocessing import StandardScaler
import pandas as pd

def scale_standard(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    '''
    Applies standard scaling (mean=0, std=1) to specified columns.

    :param df: DataFrame – input dataframe
    :param cols: list – columns to scale
    :return: scaled_df: pd.DataFrame with scaled columns
    '''

    scaler = StandardScaler()
    df_scaled = df.copy()
    df_scaled[cols] = scaler.fit_transform(df[cols])
    return df_scaled