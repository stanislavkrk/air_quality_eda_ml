from sklearn.impute import SimpleImputer

def simple_imputer(df):

    X = df.iloc[:, 2:15]
    imputer = SimpleImputer(strategy='median')
    imputer.fit(X)
    X_imputed = imputer.transform(X)
    df.iloc[:, 2:15] = X_imputed
    return df