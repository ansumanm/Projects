import numpy as np
import pickle

from sklearn.linear_model import SGDClassifier

with open('SGDClassifer_object.pkl', 'rb') as infile:
    sgd_clf = pickle.load(infile)

with open('encoder.pkl', 'rb') as infile:
    encoder = pickle.load(infile)

def dec_to_bin_conv(x):
    """
    Helper function to convert a number 
    to its fixed width binary representation
    """
    a = format(x, '032b')
    l = list(str(a))
    l = np.array(list(map(int, l)))
    return l

number  = input("Please input number:")
input_number = dec_to_bin_conv(int(number))
input_to_model = np.array([input_number])
prediction = sgd_clf.predict(input_to_model)

print(encoder.inverse_transform(prediction))

