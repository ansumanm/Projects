"""
The aim of the program is to train a single neuron to act as a NOT gate.
That is, if 1 is input, its output is 0. If 0 is input, its output is 1.

Bookmarks: 
    https://keras.io/activations/
"""
import sys
import numpy as np

from keras.models import Sequential
from keras.layers import Dense, Activation
import keras.backend as K

import matplotlib.pyplot as plt

# fix random seed for reproducibility
seed = 7
np.random.seed(seed)

"""
Our training data
"""
X_train = np.random.randint(2, size=100000)
Y_train = 1 - X_train

# Create the model.
model = Sequential()
# model.add(Dense(1, input_shape=(1,), activation=None))
model.add(Dense(1, input_shape=(1,), activation='elu'))
# model.add(Activation('softmax'))
# model.add(Activation('relu'))
# model.add(Activation('tanh'))
# model.add(Activation('sigmoid'))

# This is a binary classification problem as the output is either 0 or 1
"""
model.compile(optimizer='rmsprop',
        loss='binary_crossentropy',
        metrics=['accuracy'])
model.compile(optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy'])
"""

model.compile(optimizer='adam',
        loss='mse',
        metrics=['accuracy'])
# Train the model
try:
    # history = model.fit(X_train, Y_train, validation_split=0.25, epochs=10, verbose=1)
    history = model.fit(X_train, Y_train, epochs=10, verbose=1)
    """
    # Plot training & validation accuracy values
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    # plt.show()

    # Plot training & validation loss values
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    # plt.show()
    """
except Exception as e:
    print("{}".format(e))
    sys.exit(0)

X_test = np.array([1,1,0,0,1,1,1,1,0,1,0,1]) # Input
Y_test = np.array([0,0,1,1,0,0,0,0,1,0,1,0]) # Real output

# Evaluate the model
score = model.evaluate(X_test, Y_test)
print("Score: {}".format(score))

# Predict
predictions = []
for input_data in X_test:
    prediction = model.predict(np.array([input_data]))
    predictions.append(prediction.item(0))

print("Predicted output: {}".format(predictions))
print("Real output: {}".format(Y_test))

print("")
print("Weights: \n")
print(model.get_weights())
