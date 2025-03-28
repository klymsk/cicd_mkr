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

def test_sorted_area(data_test):
    sorted_data = sortArea(data_test)
    assert sorted_data[0]['country'] == 'Ukraine', f"Вхідне: 'Ukraine', фактичне: {sorted_data[0]['country']}"
    assert sorted_data[-1]['country'] == 'UK', f"Вхідне: 'UK', фактичне: {sorted_data[-1]['country']}"

def test_sorted_population(data_test):
    sorted_data = sortPopulation(data_test)
    assert sorted_data[0]['country'] == 'Germany', f"Вхідне: 'Germany', фактичне: {sorted_data[0]['country']}"
    assert sorted_data[-1]['country'] == 'Poland', f"Вхідне: 'Poland', фактичне: {sorted_data[-1]['country']}"


