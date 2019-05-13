import numpy as np
import pickle

def dec_to_bin_conv(x):
    """
    Helper function to convert a number 
    to its fixed width binary representation
    """
    a = format(x, '032b')
    l = list(str(a))
    l = np.array(list(map(int, l)))
    return l

def f(x):
    """
    x ==> integer
    """
    return "EVEN" if (x%2 == 0) else "ODD"

def prepare_train_dataset():
    # dataset_size = 1000000
    dataset_size = 200

    """
    x ==> integer
    """
    data = [dec_to_bin_conv(i) for i in range(dataset_size)]
    X = np.array(data)

    vect_f = np.vectorize(f)  
    Y = vect_f(np.arange(0, (dataset_size)))

    """
    Encode the EVEN/ODD
    """
    from sklearn.preprocessing import LabelEncoder
    encoder = LabelEncoder()
    encoder.fit(Y)
    encoded_Y = encoder.transform(Y)

    return X, encoded_Y, encoder


X_train, Y_train, encoder = prepare_train_dataset()
X_test = X_train
Y_test = Y_train

from sklearn.linear_model import SGDClassifier
sgd_clf = SGDClassifier(random_state=42)
sgd_clf.fit(X_train, Y_train)

with open('SGDClassifer_object.pkl', 'wb') as outfile:
    pickle.dump(sgd_clf, outfile)

with open('encoder.pkl', 'wb') as outfile:
    pickle.dump(encoder, outfile)


