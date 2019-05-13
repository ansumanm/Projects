import numpy as np

class LabelEncoderTest:
    def __init__(self):
        pass

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

    def prepare_train_dataset(self):
        # dataset_size = 100000
        dataset_size = 1000

        """
        x ==> integer
        """
        data = [LabelEncoderTest.dec_to_bin_conv(i) for i in range(dataset_size)]
        self.X = np.array(data)

        vect_f = np.vectorize(LabelEncoderTest.f)  
        self.Y = vect_f(np.arange(1, (dataset_size + 1)))

        """
        Encode the EVEN/ODD
        """
        from sklearn.preprocessing import LabelEncoder
        self.encoder = LabelEncoder()
        self.encoder.fit(self.Y)
        self.encoded_Y = self.encoder.transform(self.Y)

    def test(self):
        print(self.encoder.inverse_transform([0]))

def train(classifier):
    classifier.prepare_train_dataset()
    classifier.test()


def main():
    tester = LabelEncoderTest()
    train(tester)

if __name__ == '__main__':
    main()

