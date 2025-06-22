from cocijo.plot_series import plot_series

import pandas as pd


def test_plot_series():
    data = pd.read_csv("data/registro_lluvias.csv")
    plot_series(data)
