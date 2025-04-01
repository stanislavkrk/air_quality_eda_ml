from sklearn.preprocessing import QuantileTransformer

def quantile_transform(df, columns, output_distribution='normal', n_quantiles=1000):
    '''
    Apply QuantileTransformer to specified columns.

    :param df: DataFrame
    :param columns: list of column names to transform
    :param output_distribution: 'uniform' or 'normal' (default: 'normal')
    :param n_quantiles: number of quantiles to compute (default: 1000)
    :return: DataFrame with transformed columns
    '''

    qt = QuantileTransformer(output_distribution=output_distribution, n_quantiles=n_quantiles, random_state=42)
    df_copy = df.copy()
    df_copy[columns] = qt.fit_transform(df[columns])
    return df_copy
