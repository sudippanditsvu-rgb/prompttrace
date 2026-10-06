import json


def save_experiments(experiments):
    with open("experiments.json", "w") as f:
        json.dump(experiments, f, indent=4)

def load_experiments():
    with open("experiments.json", "r") as f:
        experiments = json.load(f)
    return experiments