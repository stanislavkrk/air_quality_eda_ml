from .regressor_interface import RegressorInterface
from statsmodels.tsa.statespace.sarimax import SARIMAX
import pandas as pd
import numpy as np

class SarimaRegressor(RegressorInterface):
    """
    SARIMA model implementation for time series forecasting.

    Methods:
        train: Fit the SARIMA model on the training time series data.
        predict: Forecast future values using the trained model.
    """

    def __init__(self, seasonal_order=(1, 1, 1, 24), order=(2, 1, 2)):
        """
        Initializes the SARIMA model with specified seasonal and non-seasonal parameters.

        :param seasonal_order: Tuple for seasonal component (P, D, Q, s).
        :param order: Tuple for ARIMA order (p, d, q).
        """
        self.order = order
        self.seasonal_order = seasonal_order
        self.model = None
        self.result = None

    def train(self, df: pd.DataFrame, target_column: str):
        """
        Trains the SARIMA model using the provided time series data.

        :param df: Time-indexed DataFrame with the target column for forecasting.
        :param target_column: Name of the column to be forecasted.
        :return: None
        """
        self.model = SARIMAX(df[target_column], order=self.order, seasonal_order=self.seasonal_order)
        self.result = self.model.fit(disp=False)

    def predict(self, steps: int) -> np.ndarray:
        """
        Forecast future values based on the trained SARIMA model.

        :param steps: Number of future time steps to forecast.
        :return: Numpy array of predicted values.
        """
        if self.result is None:
            raise ValueError("Model has not been trained yet.")
        forecast = self.result.forecast(steps=steps)
        return forecast.values
