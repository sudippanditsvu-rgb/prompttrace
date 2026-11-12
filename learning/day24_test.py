import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from storage import load_experiments
from experiment import find_experiment_by_version

experiments = load_experiments()

print("===== Experiment Search Test =====")

result = find_experiment_by_version(experiments, "v2")

if result is not None:
    print("Experiment Found!")
    print("Prompt Version:", result["prompt_version"])
    print("Model:", result["model"])
    print("Score:", result["score"])
else:
    print("Experiment Not Found!")

print("\n===== Invalid Version Test =====")

result = find_experiment_by_version(experiments, "v99")

print("Search Result:", result)