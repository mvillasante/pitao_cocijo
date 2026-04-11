import pandas as pd
import matplotlib
from streamlit.testing.v1 import AppTest

data = pd.read_csv("tests/data/registro_lluvias_for_test.csv")


def test_data_columns():
    assert "Fecha" in data.columns
    assert "mm" in data.columns


def test_streamlit_app_renders():
    at = AppTest.from_file("/workdir/cocijo/streamlit_app.py")
    at.run()
    assert not at.exception
    assert at.title[0].value == "Lluvia Diaria"
    assert len(at.subheader) == 2
