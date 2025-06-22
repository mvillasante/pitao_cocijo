import matplotlib.pyplot as plt


def plot_series(data):
    fig, ax = plt.subplots()
    line = ax.plot(data.Fecha, data.mm)
    plt.xticks(rotation=45)
    return ax
