import numpy as np

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout


class Perceptron:
    def __init__(self):
        self.classifier = Sequential()

    def initialize(self, input_shape=(1,)):
        # Adding the Single Perceptron or Shallow network
        self.classifier.add(Dense(units=1,
                                  input_shape=input_shape,
                                  activation="relu",
                                  kernel_initializer="uniform"))
        # Adding dropout to prevent overfitting
        self.classifier.add(Dropout(rate=0.1))

        # Adding the output layer
        self.classifier.add(Dense(units = 1,
                                  activation='sigmoid',
                                  kernel_initializer='uniform'))

        # criterion loss and optimizer 
        self.classifier.compile(optimizer='adam',
                                loss='binary_crossentropy',
                                metrics=['accuracy'])

    def fit(self, X_train, Y_train, batch_size, nb_epoch):
        self.classifier.fit(X_train, Y_train, batch_size, nb_epoch)

    def predict(self, X_test):
        y_pred = self.classifier.predict(X_test)
        # y_pred = (y_pred > 0.5)
        return (y_pred.astype(int))

    @staticmethod
    def confusion_matrix(y_test, y_pred):
        # Making the Confusion Matrix
        from sklearn.metrics import confusion_matrix
        cm = confusion_matrix(y_test, y_pred)
        return cm

    def save(self, file_name):
        self.classifier.save(file_name)  # creates a HDF5 file 'my_model.h5'

    def load(self, file_name):
        from keras.models import load_model
        self.classifier = load_model(file_name)

    def summary(self):
        weights, biases = self.classifier.layers[0].get_weights()
        print("weights", weights.size, weights, "biases", biases)

    def get_model(self):
        return self.classifier

    def __del__(self):
        del self.classifier

