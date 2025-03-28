import pytest
from mkr import readFile, sortArea, sortPopulation

@pytest.fixture
def data_test():
    return [
        {'country': 'Ukraine', 'area': 600000, 'population': 40000000},
        {'country': 'Poland', 'area': 500000, 'population': 35000000},
        {'country': 'Germany', 'area': 500000, 'population': 70000000},
        {'country': 'UK', 'area': 300000, 'population': 50000000}
    ]
