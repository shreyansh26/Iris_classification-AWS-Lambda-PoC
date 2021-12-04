import pytest

@pytest.fixture
def requests():
    return {
        "data": [
            [6.5, 3.0, 5.8, 2.2],
            [6.1, 2.8, 4.7, 1.2]
        ]
    }

@pytest.fixture
def response():
    return ['virginica', 'versicolor']
