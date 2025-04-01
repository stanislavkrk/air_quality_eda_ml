from sklearn.impute import KNNImputer, SimpleImputer
import pandas as pd

def knn_imputer(df: pd.DataFrame, columns: list[str], n_neighbors: int = 5) -> pd.DataFrame:
    '''
    Applies KNN imputation to specified columns in the DataFrame.

    :param df: DataFrame — input dataframe
    :param columns: list of columns to apply KNN imputation
    :param n_neighbors: int — number of neighbors for KNN
    :return: pd.DataFrame with imputed values in specified columns
    '''

    imputer = KNNImputer(n_neighbors=n_neighbors)
    df_copy = df.copy()
    imputed_array = imputer.fit_transform(df_copy[columns])
    df_copy[columns] = pd.DataFrame(imputed_array, columns=columns, index=df_copy.index)
    return df_copy

def median_imputer(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    '''
    Applies median imputation to specified columns in the DataFrame.

    :param df: pd.DataFrame — input dataframe
    :param columns: list of columns to apply median imputation
    :return: pd.DataFrame with imputed values in specified columns
    '''

    imputer = SimpleImputer(strategy='median')
    df_copy = df.copy()
    imputed_array = imputer.fit_transform(df_copy[columns])
    df_copy[columns] = pd.DataFrame(imputed_array, columns=columns, index=df_copy.index)
    return df_copy
