# Air Quality Prediction — Regression Models Comparison

This project explores and compares various regression techniques to predict the air quality indicator `C6H6(GT)` (Benzene concentration) using machine learning models.  
It is part of a data science homework assignment.

## 📁 Project Structure

```
hw04_w/
│
├── src/
│   ├── data/                          # Raw and processed datasets
│   ├── eda_tools/                     # EDA utility functions
│   ├── models/                        # Model definitions and training scripts
│   ├── prep_tools/                    # Tools for preparing data
│   ├── preprocessors/                # Data preprocessing pipeline
│   ├── visualization/                # Plotting functions and tools
│   ├── a_preprocessing.ipynb         # Initial preprocessing
│   ├── b_missing_values.ipynb        # Handling missing data
│   ├── c_exploratory_data_analysis.ipynb  # EDA
│   ├── d_preparing_to_ml.ipynb       # Feature engineering & splitting
│   └── e_machine_learning.ipynb      # Model training & evaluation
│
└── venv/                              # Virtual environment (not included in repo)
```

## ⚙️ Models Used

- **Linear Regression**
- **Ridge Regression**
- **Lasso Regression**
- **Random Forest Regressor**

## 📊 Results

| Model         | MSE     | R² Score |
|---------------|---------|----------|
| Linear        | 0.0598  | 0.9411   |
| Ridge         | 0.0598  | 0.9412   |
| Lasso         | 0.1083  | 0.8933   |
| Random Forest | 0.1083  | 0.9796   |

## 📝 Interpretation

- **Linear & Ridge Regression** performed almost identically in MSE, with Ridge giving a slightly better R².
- **Lasso Regression** was weaker, likely due to its nature of zeroing out coefficients (possible loss of useful features).
- **Random Forest** achieved the best R² score, showing its ability to model complex patterns, but with slightly worse MSE — possibly due to overfitting or less stable prediction behavior.

## ▶ Conclusion

Random Forest shows the strongest pattern recognition in this task, but Ridge and Linear models are more stable in terms of error.  
The results highlight the importance of balancing bias, variance, and model complexity.

## 🎬 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hw04_w.git
   cd hw04_w
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run Jupyter notebooks in the following order:
   - `a_preprocessing.ipynb`
   - `b_missing_values.ipynb`
   - `c_exploratory_data_analysis.ipynb`
   - `d_preparing_to_ml.ipynb`
   - `e_machine_learning.ipynb`
