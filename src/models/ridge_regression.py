from .regressor_interface import RegressorInterface
from sklearn.linear_model import Ridge

class RidgeRegressionModel(RegressorInterface):
    """
    Ridge Regression model wrapper implementing the RegressorInterface.
    This class encapsulates the scikit-learn Ridge model with L2 regularization.
    """

    def __init__(self, alpha=1.0):
        """
        Initializes the Ridge Regression model.

        :param alpha: Regularization strength (default is 1.0).
        """
        self.model = Ridge(alpha=alpha)

    def train(self, X_train, y_train):
        """
        Trains the Ridge Regression model.

        :param X_train: Training feature set.
        :param y_train: Target values for training.
        :return: None
        """
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        """
        Predicts target values using the trained Ridge Regression model.

        :param X_test: Input features for prediction.
        :return: Predicted values.
        """
        return self.model.predict(X_test)