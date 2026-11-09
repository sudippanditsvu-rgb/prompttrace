import json



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

    with open("experiments.json", "w") as f:
        json.dump(existing_experiments, f, indent=4)


def load_experiments():
    with open("experiments.json", "r") as f:
        experiments = json.load(f)
    return experiments