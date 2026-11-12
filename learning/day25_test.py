import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from storage import load_experiments
from experiment import filter_experiments_by_evaluation

experiments = load_experiments()

print("===== Good Score Experiments =====")

good_experiments = filter_experiments_by_evaluation(
    experiments,
    "Good Score"
)

for experiment in good_experiments:
    print(
        experiment["prompt_version"],
        experiment["score"]
    )

print("\n===== Needs Improvement Experiments =====")

poor_experiments = filter_experiments_by_evaluation(
    experiments,
    "Needs Improvement"
)

for experiment in poor_experiments:
    print(
        experiment["prompt_version"],
        experiment["score"]
    )