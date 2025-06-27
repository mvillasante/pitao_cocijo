from cocijo.plot_series import plot_series

import pandas as pd
import matplotlib


def test_plot_series():
    data = pd.read_csv("data/registro_lluvias.csv")
    obtained = plot_series(data)
    assert isinstance(obtained, matplotlib.axes._axes.Axes)
    assert obtained.get_xticklabels()[1].get_rotation() == 90
    matplotlib.pyplot.savefig("prueba.png")
    assert obtained.get_ylabel() == "Lluvia díaria (mm)"
    assert obtained.get_lines()[0].get_marker() == "o"
