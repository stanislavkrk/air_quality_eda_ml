import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def outliers_box (df, exclude=['DateTime', 'Hour', 'Date', 'Time']):
    numeric_cols = df.select_dtypes(include=np.number).columns
    features = [col for col in numeric_cols if col not in exclude]

    n = len(features)
    cols = 6
    rows = int(np.ceil(n / cols))

    fig, axes = plt.subplots(rows, cols, figsize=(cols * 4, rows * 8))
    axes = axes.flatten()

    for i, col in enumerate(features):
        sns.boxplot(data=df, y=col, ax=axes[i], color='skyblue')
        axes[i].set_title(col)
        axes[i].set_xlabel('')
        axes[i].grid(True)

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()
