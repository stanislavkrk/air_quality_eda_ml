from .regressor_interface import RegressorInterface
from .linear_regression import LinearRegressionModel
from .ridge_regression import RidgeRegressionModel
from .lasso_regression import LassoRegressionModel
from .random_forest import RandomForestModel
from .sarima import SarimaRegressor


class RegressorSwitch:
    """
    A unified regressor interface for handling multiple regression models.
    This class wraps different regression models (Linear, Ridge, Lasso, Random Forest, SARIMA),
    allowing standardized training and prediction workflow.
    """

    def __init__(self, model_type='linear'):
        """
        Initializes the regressor with the specified model.

        :param model_type: Type of model to use:
                           'linear' - Linear Regression,
                           'ridge' - Ridge Regression,
                           'lasso' - Lasso Regression,
                           'rf' - Random Forest Regressor,
                           'sarima' - Seasonal ARIMA (time series only).
        :raises ValueError: If the model type is unknown.
        :raises TypeError: If the selected model does not implement RegressorInterface.
        """
        match model_type:
            case 'linear':
                self.model = LinearRegressionModel()
            case 'ridge':
                self.model = RidgeRegressionModel()
            case 'lasso':
                self.model = LassoRegressionModel()
            case 'rf':
                self.model = RandomForestModel()
            case 'sarima':
                self.model = SarimaRegressor()
            case _:
                raise ValueError(f"Unknown model type: {model_type}. Choose from 'linear', 'ridge', 'lasso', 'rf', or 'sarima'.")

        if not isinstance(self.model, RegressorInterface):
            raise TypeError(f"{type(self.model).__name__} must implement RegressorInterface!")

    def train(self, X_train, y_train=None):
        """
        Trains the selected model.

        :param X_train: Feature matrix or time series dataframe (for SARIMA).
        :param y_train: Target values (ignored for SARIMA).
        :return: None
        """
        if isinstance(self.model, SarimaRegressor):
            self.model.train(X_train, target_column='C6H6(GT)')
        else:
            self.model.train(X_train, y_train)

    def predict(self, X_test):
        """
        Generates predictions using the trained model.

        :param X_test: Input data for prediction (steps for SARIMA).
        :return: Numpy array of predicted values.
        """
        return self.model.predict(X_test)
