from src.train import Classifier

cls = Classifier()

def lambda_handler(event, context):
    try:
        return cls.load_and_test(event)
    except Exception as e:
        raise