import matplotlib.pyplot as plt
import pandas as pd


def plot_cumulative(raw_data):
    data = setup_data(raw_data)
    fig, ax = plt.subplots()
    ax.plot(data.mm.cumsum(), marker=".", markersize=5)
    setup_xticks(ax)
    plt.xticks(rotation=90)
    plt.ylabel("Lluvia acumulada (mm)")
    plt.tight_layout()
    return ax


def plot_series(raw_data):
    data = setup_data(raw_data)
    fig, ax = plt.subplots()
    ax.plot(data.mm, marker="o", linestyle="", markersize=2)
    setup_xticks(ax)
    plt.xticks(rotation=90)
    plt.ylabel("Lluvia díaria (mm)")
    plt.tight_layout()
    return ax


def setup_data(raw_data):
    data = raw_data.copy()
    data["Fecha"] = pd.to_datetime(data["Fecha"], format="%Y-%m-%d")
    data["MesDia"] = data["Fecha"].dt.strftime("%m-%d")
    data.set_index("Fecha", inplace=True)
    full_date = pd.date_range(start=data.index.min(), end=data.index.max())
    data = data.reindex(full_date, fill_value=0)
    return data


def setup_xticks(ax):
    labels = [
        pd.to_datetime(label.get_text(), format="%Y-%m").month_name()
        for label in ax.get_xticklabels()
    ]
    positions = [label.get_position()[0] for label in ax.get_xticklabels()]
    ax.set_xticks(positions, labels)
