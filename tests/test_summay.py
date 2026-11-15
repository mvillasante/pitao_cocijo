from cocijo.summary import get_five_numbers, render_template

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


def test_render_template():
    template_path = "tests/data/README_for_tests.md"
    summary_variables = {"median": 123}
    obtained = render_template(template_path, summary_variables)
    assert "123" in obtained
