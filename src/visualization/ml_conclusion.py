import matplotlib.pyplot as plt
import numpy as np

def ml_conclusion(mse_lin, r2_lin, mse_rid, r2_rid, mse_las, r2_las, mse_raf, r2_raf):

    models = ['Linear', 'Lasso', 'Ridge', 'Random Forest']

    # Values
    mse_values = [mse_lin, mse_rid, mse_las, mse_raf]
    r2_values = [r2_lin, r2_rid, r2_las, r2_raf]

    # Plot figure
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # MSE
    color = 'tab:green'
    ax1.set_xlabel('Models')
    ax1.set_ylabel('MSE (lower is better)', color=color)
    ax1.bar(models, mse_values, color=color, alpha=0.6, label='MSE')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_ylim(0, max(mse_values) + 0.02)

    # R²
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('R² Score (higher is better)', color=color)
    ax2.plot(models, r2_values, color=color, marker='o', label='R² Score')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_ylim(min(r2_values) - 0.02, 1.01)

    # Grid, titles
    plt.title('Model Performance Comparison (MSE and R² Score)')
    fig.tight_layout()
    plt.grid(True, axis='y', linestyle='--', alpha=0.4)
    plt.show()
