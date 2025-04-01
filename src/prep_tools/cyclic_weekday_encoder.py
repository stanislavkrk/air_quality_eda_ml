import numpy as np
import pandas as pd

def encode_weekday_cyclic(df: pd.DataFrame, weekday_column: str = "Weekday") -> pd.DataFrame:
    '''
    Applies cyclic (revolver-style) encoding to the weekday column.

    This transformation maps the weekday values into two features using sine and cosine functions
    to preserve the cyclical nature of the days of the week (e.g., Monday and Sunday are close).

    :param df: Input DataFrame containing a weekday column with integer values (0 = Monday, ..., 6 = Sunday).
    :param weekday_column: Name of the weekday column to encode. Default is "Weekday".
    :return: A new DataFrame with added 'Weekday_sin' and 'Weekday_cos' columns, and the original weekday column removed.
    '''
    if weekday_column not in df.columns:
        raise ValueError(f"Column '{weekday_column}' not found in DataFrame")

    df['Weekday_sin'] = np.sin(2 * np.pi * df[weekday_column] / 7)
    df['Weekday_cos'] = np.cos(2 * np.pi * df[weekday_column] / 7)

    return df.drop(columns=[weekday_column])
