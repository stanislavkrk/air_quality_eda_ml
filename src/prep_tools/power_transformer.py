from sklearn.preprocessing import PowerTransformer
import pandas as pd

def power_transform(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    '''
    Apply Yeo-Johnson power transformation to reduce skewness in the selected features.

    :param df: pd.DataFrame. The input DataFrame containing numeric features.
    :param columns: list of str. The names of the columns to apply the transformation to.
    :return: pd.DataFrame. A new DataFrame with transformed features (original columns are replaced).
    '''

    df_copy = df.copy()
    pt = PowerTransformer(method='yeo-johnson', standardize=True)
    df_copy[columns] = pt.fit_transform(df_copy[columns])

    return df_copy
