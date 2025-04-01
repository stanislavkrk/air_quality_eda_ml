import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_scaled(scaled_df, columns, cols=5):

    rows = int(np.ceil(len(columns) / cols))
    fig, axes = plt.subplots(rows, cols, figsize=(cols * 5, rows * 4))
    axes = axes.flatten()

    for i, col in enumerate(columns):
        sns.kdeplot(scaled_df[col], ax=axes[i], color='steelblue', fill=True)
        axes[i].set_title(f'{col} (scaled)')
        axes[i].grid(True)

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()
