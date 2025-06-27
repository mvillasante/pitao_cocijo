import matplotlib.pyplot as plt
import pandas as pd


def plot_series(data):
    fig, ax = plt.subplots()
    data["Fecha"] = pd.to_datetime(data["Fecha"], format="%Y-%m-%d")
    ax.plot(data.Fecha, data.mm, marker="o")
    plt.xticks(rotation=90)
    plt.ylabel("Lluvia díaria (mm)")
    plt.tight_layout()
    return ax
