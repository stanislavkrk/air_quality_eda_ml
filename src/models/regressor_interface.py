from abc import ABC, abstractmethod

class RegressorInterface(ABC):
    """
    Abstract base class for all regression models.
    """

    @abstractmethod
    def train(self, X_train, y_train):
        """
        Trains the model using the provided dataset.

        :param X_train: Training feature set (image data).
        :param y_train: Corresponding labels for training data.
        :return: None
        """
        pass

    @abstractmethod
    def predict(self, X_test):
        """
        Generates predictions using the trained model.

        :param X_test: Feature set (image data) for testing.
        :return: Predicted class labels or None if the model is not trained.
        """
        pass
