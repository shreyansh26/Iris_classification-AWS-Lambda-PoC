from src.train import Classifier

cls = Classifier()


def lambda_handler(event, context):
    # event =  {
    #     "data": [
    #         [6.5, 3.0, 5.8, 2.2],
    #         [6.1, 2.8, 4.7, 1.2]
    #     ]
    # }
    try:
        return cls.load_and_test(event)
    except Exception as e:
        raise

# print(lambda_handler(None, None))