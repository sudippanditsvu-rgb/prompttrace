import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from storage import load_experiments
from experiment import delete_experiment_by_version

experiments = load_experiments()

print("Total Before Deletion:", len(experiments))

result = delete_experiment_by_version(experiments, "v3")

if result:
    print("Experiment v3 deleted successfully!")
else:
    print("Experiment Not Found!")

print("Total After Deletion:", len(experiments))