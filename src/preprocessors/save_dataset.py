import os

def save_dataframe(df, path: str, filename: str, index: bool = False, sep: str = ';'):
    '''
    Saves a pandas DataFrame to the specified directory and filename.

    :param df: pd.DataFrame — the dataframe to save
    :param path: str — relative or absolute path to the directory
    :param filename: str — name of the output file (with .csv extension)
    :param index: bool — whether to write row indices (default: False)
    :param sep: str - type of separator
    :return: None
    '''

    os.makedirs(path, exist_ok=True)  # create folder if it doesn't exist
    full_path = os.path.join(path, filename)
    df.to_csv(full_path, index=index, sep=sep)
    print(f"Dataset saved to: {full_path}")