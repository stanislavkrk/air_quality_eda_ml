import seaborn as sns
import matplotlib.pyplot as plt

def hourly_boxplot(df):

    plt.figure(figsize=(14, 6))
    sns.boxplot(data=df, x='Hour', y='C6H6(GT)', hue='Hour', dodge=False, legend=False, palette='coolwarm')

    plt.title('Distribution of C6H6(GT) by Hour of Day')
    plt.xlabel('Hour of Day')
    plt.ylabel('C6H6(GT)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()