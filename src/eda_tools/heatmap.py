import seaborn as sns
import matplotlib.pyplot as plt

def heatmap(df, target='C6H6(GT)', top_n=6):
    corr = df.corr(numeric_only=True)
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlations map")
    plt.show()

    # Correlations only with target value
    target_corr = corr[target].sort_values(ascending=False)
    print('Correlations with C6H6(GT):', target_corr)

    top_corr = corr[target].drop(labels=target).sort_values(ascending=False)

    # List with the most correlative values
    top_features = list(top_corr.head(top_n).index)
    return top_features