import numpy as np
import pandas as pd

def log_plus(df: pd.DataFrame, cols: list[str], epsilon: float = 1e-6) -> pd.DataFrame:
    '''
    Safely apply logarithmic transformation to selected columns.
    Shifts data to positive domain before applying log, avoiding negative or zero values.

    :param df: pd.DataFrame. Input dataframe.
    :param cols: list of str. List of column names to transform.
    :param epsilon: float, optional. Small value to avoid log(0), default is 1e-6.
    :return: pd.DataFrame. DataFrame with log-transformed columns.
    '''

    df_transformed = df.copy()
    for col in cols:
        min_val = df[col].min()
        shift = -min_val + epsilon if min_val <= 0 else 0
        df_transformed[col] = np.log(df[col] + shift)
    return df_transformed
