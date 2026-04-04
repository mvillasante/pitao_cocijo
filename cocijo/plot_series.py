import matplotlib.pyplot as plt
import pandas as pd
from babel.dates import format_date


def plot_yearly_rain(raw_data):
    data = setup_data(raw_data)
    fig, ax = plt.subplots()
    for year, group in data.groupby(data.Fecha.dt.year):
        ax.plot(group.dia_del_año, group.mm, marker="o", linestyle="", markersize=3, label=year)
    plt.legend()
    setup_xticks(ax)
    plt.ylabel("Lluvia diaria (mm)")
    plt.tight_layout()
    return ax


def plot_cumulative_yearly_rain(raw_data):
    data = setup_data(raw_data)
    fig, ax = plt.subplots()
    for year, group in data.groupby(data.Fecha.dt.year):
        ax.plot(
            group.dia_del_año, group.mm.cumsum(), marker="o", linestyle="", markersize=3, label=year
        )
    plt.legend()
    setup_xticks(ax)
    plt.ylabel("Lluvia acumulada (mm)")
    plt.tight_layout()
    return ax


def plot_cumulative(raw_data):
    data = setup_data(raw_data)
    fig, ax = plt.subplots()
    ax.plot(data.dia_del_año, data.mm.cumsum(), marker=".", markersize=5)
    setup_xticks(ax)
    plt.ylabel("Lluvia acumulada (mm)")
    plt.tight_layout()
    return ax


def plot_series(raw_data):
    data = setup_data(raw_data)
    fig, ax = plt.subplots()
    ax.plot(data.dia_del_año, data.mm, marker="o", linestyle="", markersize=2)
    setup_xticks(ax)
    plt.ylabel("Lluvia díaria (mm)")
    plt.tight_layout()
    return ax


def setup_data(raw_data):
    data = raw_data.copy()
    data["Fecha"] = pd.to_datetime(data["Fecha"], format="%Y-%m-%d")
    data["dia_del_año"] = data["Fecha"].dt.dayofyear
    return data


def setup_xticks(ax):
    meses = pd.date_range(start="2000-01-01", periods=12, freq="MS")
    spanish_months = [format_date(date, format="MMMM", locale="es").capitalize() for date in meses]
    ax.set_xticks(meses.day_of_year, spanish_months, rotation=90)
