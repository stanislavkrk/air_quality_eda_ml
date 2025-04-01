from .regressor_interface import RegressorInterface
from sklearn.linear_model import Lasso

class LassoRegressionModel(RegressorInterface):
    """
    Lasso Regression model wrapper implementing the RegressorInterface.
    This class encapsulates the scikit-learn Lasso model with L1 regularization.
    """

    def __init__(self, alpha=0.1):
        """
        Initializes the Lasso Regression model.

        :param alpha: Regularization strength (default is 1.0).
        """
        self.model = Lasso(alpha=alpha)

    def train(self, X_train, y_train):
        """
        Trains the Lasso Regression model.

        :param X_train: Training feature set.
        :param y_train: Target values for training.
        :return: None
        """
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        """
        Predicts target values using the trained Lasso Regression model.

        :param X_test: Input features for prediction.
        :return: Predicted values.
        """
        return self.model.predict(X_test)