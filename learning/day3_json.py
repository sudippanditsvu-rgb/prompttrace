import json
from day2_functions import experiments


with open("experiments.json", "w") as f:
    json.dump(experiments, f, indent=4)
with open("experiment.json", "r") as f:
    data = json.load(f)
print(data)


def evaluate_experiment(experiments):
    for i in experiments:
        print(i["score"])
evaluate_experiment(data)
