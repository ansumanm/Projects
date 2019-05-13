"""
The aim of the program is to train a single neuron to act as a PASS gate.
That is, if 1 is input, its output is 1. If 0 is input, its output is 0.
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
Y_train = X_train

# Create the model.
model = Sequential()
model.add(Dense(1, input_shape=(1,)))
# model.add(Activation('softmax'))
model.add(Activation('relu'))
# model.add(Activation('tanh'))
# model.add(Activation('sigmoid'))

# This is a binary classification problem as the output is either 0 or 1
model.compile(optimizer='rmsprop',
        loss='binary_crossentropy',
        metrics=['accuracy'])
"""
model.compile(optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy'])
"""

# Train the model
try:
    history = model.fit(X_train, Y_train, validation_split=0.25, epochs=10, verbose=1)
    print(history)
except Exception as e:
    print("{}".e)
    sys.exit(0)

X_test = np.array([1,1,0,0,1,1,1,1,0,1,0,1]) # Input
Y_test = X_test

# Evaluate the model
"""
score = model.evaluate(X_test, Y_test)
print("Score: {}".format(score))
"""

# Predict
predictions = []
for input_data in X_test:
    prediction = model.predict(np.array([input_data]))
    predictions.append(prediction.item(0))

print("Predicted output: {}".format(predictions))
print("Real output: {}".format(Y_test))

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
        json_file.write(model_json)

# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")
         
"""
# later...
# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")
"""
