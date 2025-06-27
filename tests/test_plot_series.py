from cocijo.plot_series import plot_series

import pandas as pd
import matplotlib


def test_plot_series():
    data = pd.read_csv("data/registro_lluvias.csv")
    obtained = plot_series(data)
    assert isinstance(obtained, matplotlib.axes._axes.Axes)
    assert obtained.get_xticklabels()[1].get_rotation() == 90
    assert obtained.get_ylabel() == "Lluvia díaria (mm)"
    obtained_first_line = obtained.get_lines()[0]
    assert obtained_first_line.get_marker() == "o"
    expected_first_date = "March"
    assert obtained.get_xticklabels()[0].get_text() == expected_first_date
    assert obtained_first_line.get_linestyle() is "None"

    matplotlib.pyplot.savefig("lluvia_diaria.png")
