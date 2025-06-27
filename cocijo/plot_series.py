import matplotlib.pyplot as plt
import pandas as pd


def plot_series(data):
    fig, ax = plt.subplots()
    data["Fecha"] = pd.to_datetime(data["Fecha"], format="%Y-%m-%d")
    data["MesDia"] = data["Fecha"].dt.strftime("%m-%d")
    data.set_index("MesDia", inplace=True)
    full_dates = pd.date_range(start="1900-01-01", end="1900-12-01", freq="MS")
    data = data.reindex(full_dates.strftime("%m-%d"), fill_value=0)

    ax.plot(full_dates, data.mm, marker="o")
    labels = [
        pd.to_datetime(label.get_text(), format="%Y-%m").month_name()
        for label in ax.get_xticklabels()
    ]
    positions = [label.get_position()[0] for label in ax.get_xticklabels()]
    ax.set_xticks(positions, labels)
    plt.xticks(rotation=90)
    plt.ylabel("Lluvia díaria (mm)")
    plt.tight_layout()
    return ax
