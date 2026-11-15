from cocijo.summary import get_five_numbers

import pandas as pd


def test_get_five_numbers():
    data = pd.read_csv("tests/data/registro_lluvias_for_test.csv")
    obtained = get_five_numbers(data)
    assert isinstance(obtained, dict)
    obtained_keys = obtained.keys()
    assert set(["min", "q1", "median", "q3", "max"]) == obtained_keys
    expected_max = 90
    expected_min = 2
    expected_q1 = 5
    expected_median = 11
    expected_q3 = 28
    assert obtained["max"] == expected_max
    assert obtained["min"] == expected_min
    assert obtained["q1"] == expected_q1
    assert obtained["median"] == expected_median
    assert obtained["q3"] == expected_q3
