
def comas_to_float(df):

    df['C6H6(GT)'] = df['C6H6(GT)'].map(lambda x: float(x.replace(',', '.')))
    df['CO(GT)'] = df['CO(GT)'].map(lambda x: float(x.replace(',', '.')))
    df['T'] = df['T'].map(lambda x: float(x.replace(',', '.')))
    df['RH'] = df['RH'].map(lambda x: float(x.replace(',', '.')))
    df['AH'] = df['AH'].map(lambda x: float(x.replace(',', '.')))
    return df