import numpy as np
from scipy.sparse.construct import spdiags
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pickle
import pandas as pd


class Model:
    def __init__(self):
        pass

    @staticmethod
    def train_and_save(self):
        iris = load_iris()
        ada = AdaBoostClassifier(n_estimators=5)

        X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.1)
        model = ada.fit(X_train, y_train)

        print("Model score: ", ada.score(X_train, y_train))
        print("Test Accuracy: ", ada.score(X_test, y_test))

        pd.concat([pd.DataFrame(X_test), pd.DataFrame(y_test, columns=['4'])], axis=1).to_csv('test_data.csv', index=False)

        pickle.dump(model, open("../models/model.pkl", "wb"))