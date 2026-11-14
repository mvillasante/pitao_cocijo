from cocijo.plot_series import (
    plot_series,
    plot_cumulative,
    setup_data,
    plot_yearly_rain,
)

import matplotlib
import pandas as pd

data = pd.read_csv("tests/data/registro_lluvias_for_test.csv")


def tests_plot_yearly_rain():
    obtained = plot_yearly_rain(data)
    obtained_lines = obtained.get_lines()
    assert len(obtained_lines) == 2


def test_plot_series():
    obtained = plot_series(data)
    assert isinstance(obtained, matplotlib.axes._axes.Axes)
    assert obtained.get_xticklabels()[1].get_rotation() == 90
    assert obtained.get_ylabel() == "Lluvia díaria (mm)"
    obtained_first_line = obtained.get_lines()[0]
    assert obtained_first_line.get_marker() == "o"
    assert obtained_first_line.get_markersize() == 2
    expected_first_date = "Enero"
    assert obtained.get_xticklabels()[0].get_text() == expected_first_date
    assert obtained_first_line.get_linestyle() == "None"
    assert all(obtained.get_children()[0].get_xdata()) < 365


def test_plot_cumulative():
    obtained = plot_cumulative(data)
    obtained_first_line = obtained.get_lines()[0]
    assert max(obtained_first_line.get_data()[1]) > data.mm.max()
    assert obtained_first_line.get_marker() == "."
    assert obtained.get_ylabel() == "Lluvia acumulada (mm)"
    assert obtained_first_line.get_markersize() == 5
    assert obtained.get_children()[0].get_xdata()[0] == 48


def test_setup_data():
    obtained = setup_data(data)
    is_here_nan = obtained.mm.isna().any()
    assert not is_here_nan
    expected_columns = set(["dia_del_año", "mm", "Fecha"])
    assert set(obtained.columns) == expected_columns
