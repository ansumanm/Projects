import sys
import numpy as np
from perceptron import Perceptron

"""
print("X[1:2]: ", X[1:2])
scores = model.predict(X[1:2])
print(scores)
print(np.argmax(scores))
"""

def dec_to_bin_conv(x):
  a = format(x, '032b')
  l = list(str(a))
  l = np.array(list(map(int, l)))
  return l

number  = input("Please input number:")
input_number = dec_to_bin_conv(int(number))
input_to_model = np.array([input_number])

# Load the trained instance
model = Perceptron()
model.load('odd_even_classifier_model.h5')

scores = model.predict(input_to_model)
print(scores)
