import numpy as np
import pickle
from perceptron import Perceptron

class Odd_Even_Classifier(Perceptron):
    def __init__(self):
        super().__init__()
        super().initialize(input_shape=(32,))

    @staticmethod
    def dec_to_bin_conv(x):
        """
        Helper function to convert a number 
        to its fixed width binary representation
        """
        a = format(x, '032b')
        l = list(str(a))
        l = np.array(list(map(int, l)))
        return l

    @staticmethod
    def f(x):
        """
        x ==> integer
        """
        return "EVEN" if (x%2 == 0) else "ODD"

    @staticmethod
    def get_X_Y():
        dataset_size = 10000
        # dataset_size = 1000

        """
        x ==> integer
        """
        data = [Odd_Even_Classifier.dec_to_bin_conv(i) for i in range(dataset_size)]
        X = np.array(data)

        vect_f = np.vectorize(Odd_Even_Classifier.f)  
        Y = vect_f(np.arange(0, (dataset_size)))

        from sklearn.preprocessing import LabelEncoder
        encoder = LabelEncoder()
        encoder.fit(Y)
        encoded_Y = encoder.transform(Y)

        return X, encoded_Y

    def prepare_train_dataset(self):
        dataset_size = 1000000
        # dataset_size = 1000

        """
        x ==> integer
        """
        data = [Odd_Even_Classifier.dec_to_bin_conv(i) for i in range(dataset_size)]
        self.X = np.array(data)

        vect_f = np.vectorize(Odd_Even_Classifier.f)  
        self.Y = vect_f(np.arange(0, (dataset_size)))

        """
        Encode the EVEN/ODD
        """
        self.encoder = LabelEncoder()
        self.encoder.fit(self.Y)
        self.encoded_Y = self.encoder.transform(self.Y)

    def fit(self):
        super().fit(self.X, self.encoded_Y, batch_size=10000, nb_epoch=1000)

    def save(self):
        super().save("odd_even_classifier_model.h5")

        with open('encoder.pkl', 'wb') as outfile:
            pickle.dump(self.encoder, outfile)


    def load(self):
        super().load("odd_even_classifier_model.h5")

        with open('encoder.pkl', 'rb') as infile:
            self.encoder = pickle.load(infile)

    def predict(self):
        number  = input("Please input number:")
        input_number = Odd_Even_Classifier.dec_to_bin_conv(int(number))
        input_to_model = np.array([input_number])
        scores = super().predict(input_to_model)
        return (self.encoder.inverse_transform(scores))

def train(classifier):
    classifier.prepare_train_dataset()
    classifier.fit()
    classifier.save()

def test(classifier):
    classifier.load()
    classifier.summary()
    scores = classifier.predict()
    print(scores)

def main():
    classifier = Odd_Even_Classifier()
    # train(classifier)
    test(classifier)

if __name__ == '__main__':
    main()

