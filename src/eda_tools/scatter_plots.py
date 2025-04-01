import seaborn as sns
import matplotlib.pyplot as plt
import math

def scatter_plots(top_features, df, target='C6H6(GT)', cols=3):

    rows = math.ceil(len(top_features) / cols)
    fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 4 * rows))
    axes = axes.flatten()

    for i, col in enumerate(top_features):
        sns.scatterplot(data=df, x=col, y=target, ax=axes[i])
        axes[i].set_title(f'{target} vs {col}')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel(target)
        axes[i].grid(True)

    plt.tight_layout()
    plt.show()
