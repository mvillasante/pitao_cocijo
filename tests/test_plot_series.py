from cocijo.plot_series import plot_series, plot_cumulative

import pandas as pd
import matplotlib


data = pd.read_csv("data/registro_lluvias.csv")


def test_plot_series():
    obtained = plot_series(data)
    assert isinstance(obtained, matplotlib.axes._axes.Axes)
    assert obtained.get_xticklabels()[1].get_rotation() == 90
    assert obtained.get_ylabel() == "Lluvia díaria (mm)"
    obtained_first_line = obtained.get_lines()[0]
    assert obtained_first_line.get_marker() == "o"
    expected_first_date = "March"
    assert obtained.get_xticklabels()[0].get_text() == expected_first_date
    assert obtained_first_line.get_linestyle() == "None"

    matplotlib.pyplot.savefig("lluvia_diaria.png")


def test_plot_cumulative():
    obtained = plot_cumulative(data)
    obtained_first_line = obtained.get_lines()[0]
    assert max(obtained_first_line.get_data()[1]) > data.mm.max()
    assert obtained_first_line.get_marker() == "."
    matplotlib.pyplot.savefig("lluvia_acumulada.png")
