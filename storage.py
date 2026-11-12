import json



DATA_FILE = "data/experiments.json"


def save_experiments(experiments):
    try:
        existing_experiments = load_experiments()
    except FileNotFoundError:
        existing_experiments = []

    for new_experiment in experiments:
        duplicate = False

        for old_experiment in existing_experiments:
            if (
                old_experiment["prompt_version"]
                == new_experiment["prompt_version"]
            ):
                duplicate = True
                break

        if not duplicate:
            existing_experiments.append(new_experiment)

    with open(DATA_FILE, "w") as f:
        json.dump(existing_experiments, f, indent=4)


def load_experiments():
    with open(DATA_FILE, "r") as f:
        experiments = json.load(f)

    return experiments

def update_experiments(experiments):

    with open(DATA_FILE, "w") as file:
        json.dump(experiments, file, indent=4)