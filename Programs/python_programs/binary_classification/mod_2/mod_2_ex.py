import sys
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical


# Helper function to convert a number 
# to its fixed width binary representation
def conv(x):
  a = format(x, '032b')
  l = list(str(a))
  l = np.array(list(map(int, l)))
  return l

# input data
data = [conv(i) for i in range(100000)]
X = np.array(data)

print(X)

Y= list() # empty list of results
for v in range(100000):
  Y.append( to_categorical(v%2, 2) )

Y = np.array(Y) # we need np.array
print(Y)

# Sequential is a fully connected network
model = Sequential()

# 32 inputs and 1 neuron in the first layer (hidden layer)
model.add(Dense(1, input_dim=32, activation='relu'))

# 2 output layer 
model.add(Dense(2, activation='sigmoid'))


model.compile(loss='binary_crossentropy', 
              optimizer='adam', 
              metrics=['accuracy'])

# epochs is the number of times to retrain over the same data set
# batch_size is how may elements to process in parallel at one go
model.fit(X, Y, epochs=5, batch_size=100, verbose=1)
weights, biases = model.layers[0].get_weights()
print("weights",weights.size, weights, "biases", biases)
model.summary()

print("X[0:1]: ", X[0:1])
scores = model.predict(X[0:1])
print(scores)
print(np.argmax(scores))

print("X[1:2]: ", X[1:2])
scores = model.predict(X[1:2])
print(scores)
print(np.argmax(scores))
