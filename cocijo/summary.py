def get_five_numbers(data):
    return {
        "min": data["mm"].min(),
        "q1": data.mm.quantile(0.25),
        "median": data.mm.median(),
        "q3": data.mm.quantile(0.75),
        "max": data["mm"].max(),
    }
