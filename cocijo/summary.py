from jinja2 import Environment, FileSystemLoader
import os


def render_template(template_path, summary):
    environment = Environment(loader=FileSystemLoader(os.path.abspath(".")))
    template = environment.get_template(template_path)
    return template.render(summary)


def get_five_numbers(data):
    return {
        "min": data["mm"].min(),
        "q1": data.mm.quantile(0.25),
        "median": data.mm.median(),
        "q3": data.mm.quantile(0.75),
        "max": data["mm"].max(),
    }
