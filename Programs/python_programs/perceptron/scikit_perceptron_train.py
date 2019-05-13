import numpy as np
from perceptron import Perceptron

# Helper function to convert a number 
# to its fixed width binary representation
def dec_to_bin_conv(x):
  a = format(x, '032b')
  l = list(str(a))
  l = np.array(list(map(int, l)))
  return l

def main():
    # Prepare dataset
    dataset_size = 100000

    # input data
    data = [dec_to_bin_conv(i) for i in range(dataset_size)]
    X = np.array(data)
    print(X)
    print(X.shape)
    print(type(X))

    """
    Y = list() # empty list of results
    for v in range(dataset_size):
        Y.append(to_categorical(v%2, 2))
    Y = np.array(Y)
    print(Y)
    print(Y.shape)
    print(type(Y))
    sys.exit(0)
    """
    def f(x):
        return "EVEN" if (x%2 == 0) else "ODD"

    f = np.vectorize(f)  
    Y = f(np.arange(1, (dataset_size + 1)))

    # print(X, Y)

    # encode class values as integers
    from sklearn.preprocessing import LabelEncoder
    encoder = LabelEncoder()
    encoder.fit(Y)
    encoded_Y = encoder.transform(Y)

    # Create the Perceptron instance
    model = Perceptron()
    model.initialize(input_shape=(32,))

    # Fit
    model.fit(X, encoded_Y, batch_size=100, nb_epoch=1000)

    # Save
    model.save("odd_even_classifier_model.h5")


if __name__ == '__main__':
    main()
