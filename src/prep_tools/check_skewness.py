import pandas as pd
from scipy.stats import skew

def check_skewness(df, threshold=0.5):
    '''
    Computes skewness for all numeric columns in the DataFrame.

    :param df: pd.DataFrame. Input DataFrame containing the features.
    :param threshold: float, optional (default=0.5).
        Absolute skewness threshold above which a feature is considered skewed.
    :return: pd.DataFrame
        A table with skewness values and a boolean flag indicating whether
        each feature is skewed beyond the threshold.
    '''

    numeric_cols = df.select_dtypes(include='number').columns
    skewness_values = df[numeric_cols].apply(lambda x: skew(x.dropna()))

    result = pd.DataFrame({
        'Skewness': skewness_values,
        'Skewed': skewness_values.abs() > threshold
    }).sort_values(by='Skewness', key=lambda x: x.abs(), ascending=False)

    return result
