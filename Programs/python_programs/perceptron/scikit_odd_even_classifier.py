import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from odd_even_classifier import Odd_Even_Classifier


def create_baseline():
    classifier = Odd_Even_Classifier()
    model = classifier.get_model()

def main():
    # fix random seed for reproducibility
    seed = 7
    np.random.seed(seed)

    estimator =  KerasClassifier(build_fn=create_baseline,
                                 epochs=100,
                                 batch_size=5,
                                 verbose=1)

    X, encoded_Y = Odd_Even_Classifier.get_X_Y()

    kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
    results = cross_val_score(estimator, X, encoded_Y, cv=kfold)
    print("Results: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
    # train(classifier)
    # test(classifier)

if __name__ == '__main__':
    main()


