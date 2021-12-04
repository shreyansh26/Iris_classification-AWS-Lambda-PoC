import pickle
from src.model import Model

class Classifier:
    def __init__(self):
        pass

    def train(self):
        model = Model()
        model.train_and_save()

    def load_and_test(self, data):
        # data = {
        #         "data": [
        #             [5.5, 4.2, 1.4, 0.2],
        #             [6.1, 2.8, 4.7, 1.2]
        #         ]
        #     }
        
        iris_types = {
                0: 'setosa',
                1: 'versicolor',
                2: 'virginica'
            }

        model = pickle.load(open("models/model.pkl", "rb"))

        prediction = list(map(lambda x: iris_types[x], model.predict(data["data"]).tolist()))
        log_proba = model.predict_log_proba(data["data"]).tolist()

        return {"prediction": prediction, "log_proba": log_proba}