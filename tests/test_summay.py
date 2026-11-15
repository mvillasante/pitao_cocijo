from cocijo.summary import get_five_numbers

import pandas as pd


def test_get_five_numbers():
    data = pd.read_csv("tests/data/registro_lluvias_for_test.csv")
    obtained = get_five_numbers(data)
    assert isinstance(obtained, dict)
    obtained_keys = obtained.keys()
    assert set(["min", "q1", "median", "q3", "max"]) == obtained_keys
