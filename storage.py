import json
from database import (
    create_table,
    insert_experiment,
    fetch_all_experiments
)



DATA_FILE = "data/experiments.json"


def save_experiments(experiments):

    create_table()

    saved = 0
    for experiment in experiments:

        if "created_at" not in experiment:
            from datetime import datetime

            experiment["created_at"] = datetime.now().isoformat(
                timespec="seconds"
            )
        if insert_experiment(experiment):
            saved += 1

    return saved


def load_experiments():

    create_table()
    return fetch_all_experiments()

def update_experiments(experiments):

    with open(DATA_FILE, "w") as file:
        json.dump(experiments, file, indent=4)