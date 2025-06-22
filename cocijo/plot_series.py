import matplotlib.pyplot as plt


def plot_series(data):
    fig, ax = plt.subplots()
    ax.plot(data.Fecha, data.mm, marker="o")
    plt.xticks(rotation=90)
    plt.ylabel("Lluvia díaria (mm)")
    plt.tight_layout()
    return ax
