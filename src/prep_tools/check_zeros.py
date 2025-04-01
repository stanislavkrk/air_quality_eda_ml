def check_zeros(df, cols):
    '''
    Print the number of zero values in each of the specified columns.

    :param df: The DataFrame to check.
    :param cols: List of columns to analyze.
    :return: None
    '''

    zero_counts = (df[cols] == 0).sum()
    print("Zero values per column:")
    print(zero_counts[zero_counts > 0])
