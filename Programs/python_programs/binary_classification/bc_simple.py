"""
Again we pick up a simple task:
Classify the numbers into odd and even number.
It can't get simpler than this, can it?
"""
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from keras.layers import Activation
from keras.utils.generic_utils import get_custom_objects

"""
Custom activation functions.
"""
def mod(x):
    return (x%2)

get_custom_objects().update({'mod': Activation(mod)})

"""
Custom activation functions END.
"""

# fix random seed for reproducibility
seed = 7
np.random.seed(seed)

# Dataset preparation
X = np.arange(1, 10000)
# X = np.arange(1, 10)
np.random.shuffle(X)

# We now have an array with element n , 1 <= n < 100000
# Our output variable will have the string either ODD or EVEN.
# We will use the numpy vectorize vectorize function to generate
# output dataset.
def f(x):
    return "EVEN" if (x%2 == 0) else "ODD"

f = np.vectorize(f)  
Y = f(X)  

# print(X, Y)

# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)

# print(encoded_Y)

# baseline model
def create_baseline():
    # create model
    model = Sequential()

    # Hidden layer which has the same number of neurons as input variables.
    # The weights are initialized using a small Gaussian random number.
    model.add(Dense(1, input_shape=(1,), kernel_initializer='normal', activation='mod'))

    # model.add(Dense(1, kernel_initializer='normal', activation='elu'))
    # The output layer contains a single layer to make predictions.
    # It uses the sigmoid activation function in order to produce a probability
    # output in the range of 0 to 1 that can easily and automatically be
    # converted to crisp class values.
    model.add(Dense(1, kernel_initializer='normal', activation='relu'))
    # model.add(Dense(1, kernel_initializer='normal', activation='linear'))
    # model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))

    # Compile model
    # we are using the logarithmic loss function (binary_crossentropy) during
    # training, the preferred loss function for binary classification problems.
    # The model also uses the efficient Adam optimization algorithm for
    # gradient descent and accuracy metrics will be collected when the model is
    # trained.
    # model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
    return model



"""
Now it is time to evaluate this model using stratified cross validation in the
scikit-learn framework.

To use Keras models with scikit-learn, we must use the KerasClassifier wrapper.
This class takes a function that creates and returns our neural network model.
It also takes arguments that it will pass along to the call to fit() such as
the number of epochs and the batch size.
We pass the number of training epochs to the KerasClassifier, again using
reasonable default values. Verbose output is also turned off given that the
model will be created 10 times for the 10-fold cross validation being
performed.
"""
# Rescale our data
# evaluate baseline model with standardized dataset
estimator =  KerasClassifier(build_fn=create_baseline, epochs=100, batch_size=5, verbose=1)


"""
We are going to use scikit-learn to evaluate the model using stratified k-fold
cross validation. This is a resampling technique that will provide an estimate
of the performance of the model. It does this by splitting the data into
k-parts, training the model on all parts except one which is held out as a test
set to evaluate the performance of the model. This process is repeated k-times
and the average score across all constructed models is used as a robust
estimate of performance. It is stratified, meaning that it will look at the
output values and attempt to balance the number of instances that belong to
each class in the k-splits of the data.
"""
kfold = StratifiedKFold(n_splits=1000, shuffle=True, random_state=seed)
results = cross_val_score(estimator, X, encoded_Y, cv=kfold)
print("Results: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))

"""
estimator.fit(X, Y)
prediction = estimator.predict(X)
print("Real: {}".format(Y))
print("Predicted: {}".format(prediction))
"""
