import matplotlib.pyplot as plt
import pandas as pd


def plot_yearly_rain(raw_data):
    data = setup_data(raw_data)
    fig, ax = plt.subplots()
    for year, group in data.groupby(data.index.year):
        ax.plot(group.mm, marker="o", linestyle="", markersize=2, label=year)
    plt.legend()
    plt.xticks(rotation=90)
    plt.ylabel("Lluvia diaria (mm)")
    plt.tight_layout()
    return ax


def plot_cumulative(raw_data):
    data = setup_data(raw_data)
    fig, ax = plt.subplots()
    ax.plot(data.dia_del_año, data.mm.cumsum(), marker=".", markersize=5)
    setup_xticks(ax)
    plt.xticks(rotation=90)
    plt.ylabel("Lluvia acumulada (mm)")
    plt.tight_layout()
    return ax


def plot_series(raw_data):
    data = setup_data(raw_data)
    fig, ax = plt.subplots()
    ax.plot(data.dia_del_año, data.mm, marker="o", linestyle="", markersize=2)
    setup_xticks(ax)
    plt.xticks(rotation=90)
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
    ax.set_xticks(meses.day_of_year, meses.month_name())
