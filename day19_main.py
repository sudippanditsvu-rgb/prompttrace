from storage import load_experiments
from experiment import rank_experiments

experiments = load_experiments()

ranked_experiments = rank_experiments(experiments)

print("\n===== Experiment Ranking =====")

for experiment in ranked_experiments:
    print(
        experiment["prompt_version"],
        "->",
        experiment["score"]
    )