from .regressor_interface import RegressorInterface
from sklearn.ensemble import RandomForestRegressor

class RandomForestModel(RegressorInterface):
    """
    Random Forest Regression model wrapper implementing the RegressorInterface.
    This class encapsulates the scikit-learn RandomForestRegressor model for ensemble-based regression.
    """

    def __init__(self, n_estimators=100, max_depth=None, random_state=42):
        """
        Initializes the Random Forest model with specified parameters.

        :param n_estimators: Number of trees in the forest.
        :param max_depth: Maximum depth of the tree.
        :param random_state: Random seed for reproducibility.
        """
        self.model = RandomForestRegressor(n_estimators=n_estimators,
                                           max_depth=max_depth,
                                           random_state=random_state)

    def train(self, X_train, y_train):
        """
        Trains the Random Forest Regression model.

        :param X_train: Training feature set.
        :param y_train: Target values for training.
        :return: None
        """
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        """
        Predicts target values using the trained Random Forest Regression model.

        :param X_test: Input features for prediction.
        :return: Predicted values.
        """
        return self.model.predict(X_test)