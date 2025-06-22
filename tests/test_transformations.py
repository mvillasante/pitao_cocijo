from cocijo.plot_series import plot_series

import pandas as pd
import matplotlib


def test_plot_series():
    data = pd.read_csv("data/registro_lluvias.csv")
    obtained = plot_series(data)
    assert isinstance(obtained, matplotlib.lines.Line2D)
