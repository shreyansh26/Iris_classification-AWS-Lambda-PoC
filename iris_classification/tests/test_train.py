from src.train import Classifier

pipeline = Classifier()

def test_response(requests, response):
    assert response == pipeline.load_and_test(requests)['prediction']
