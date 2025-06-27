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
    obtained_first_line = obtained.get_lines()[0]
    assert obtained_first_line.get_marker() == "o"
    assert len(obtained_first_line.get_data()[0]) == 12
    expected_first_date = "January"
    assert obtained.get_xticklabels()[0].get_text() == expected_first_date
