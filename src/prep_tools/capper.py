import numpy as np
import pandas as pd

def cap_outliers(df: pd.DataFrame, cols: list, lower_quantile=0.01, upper_quantile=0.99) -> pd.DataFrame:
    '''
    Caps outliers in specified columns based on quantiles.

    :param df: pd.DataFrame – input dataframe
    :param cols: list – list of columns to cap
    :param lower_quantile: float – lower quantile threshold (default 0.01)
    :param upper_quantile: float – upper quantile threshold (default 0.99)
    :return: df: pd.DataFrame with capped values
    '''

    df_capped = df.copy()
    for col in cols:
        lower = df[col].quantile(lower_quantile)
        upper = df[col].quantile(upper_quantile)
        df_capped[col] = df[col].clip(lower, upper)
    return df_capped