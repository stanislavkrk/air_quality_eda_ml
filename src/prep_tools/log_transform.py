import pandas as pd
import numpy as np

def log_transform(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    '''
    Applies log transformation (log(1+x)) to skewed numeric features.
    :param df: pd.DataFrame – input dataframe
    :param cols: list – columns to transform
    :return: transformed_df: pd.DataFrame with log-transformed columns
    '''

    df_transformed = df.copy()
    for col in cols:
        df_transformed[col] = np.log1p(df[col])
    return df_transformed
