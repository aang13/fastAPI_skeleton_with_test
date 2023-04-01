import pytest
from src.model.musician import Musician



@pytest.fixture
def musician_df():
    return pd.DataFrame({'name': ['kurt'],
                         'surname': ['cobain'],
                         'age': [27],
                         'instrument': ['guitar']})
def musician():
    return Musician(name='kurt',
                    surname='cobain',
                    age=27,
                    instrument='guitar')