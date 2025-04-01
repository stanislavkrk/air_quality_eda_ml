import pandas as pd

def check_missing(df):

    total = df.isna().sum()
    percent = (total / len(df)) * 100
    missing_df = pd.DataFrame({
        'Missing Count': total,
        'Missing %': percent.round(2)
    })

    missing_df = missing_df[missing_df['Missing Count'] > 0]
    return missing_df.sort_values(by='Missing Count', ascending=False)
