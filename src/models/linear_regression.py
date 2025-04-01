from .regressor_interface import RegressorInterface
from sklearn.linear_model import LinearRegression

class LinearRegressionModel(RegressorInterface):
    """
    Linear Regression model wrapper implementing the RegressorInterface.
    This class encapsulates the scikit-learn LinearRegression model for training and prediction.
    """

    def __init__(self):
        """
        Initializes the LinearRegression model.
        """
        self.model = LinearRegression()

    def train(self, X_train, y_train):
        """
        Trains the Linear Regression model.

        :param X_train: Training feature set.
        :param y_train: Target values for training.
        :return: None
        """
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        """
        Predicts target values using the trained Linear Regression model.

        :param X_test: Input features for prediction.
        :return: Predicted values.
        """
        return self.model.predict(X_test)