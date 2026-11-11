from storage import load_experiments
from experiment import compare_experiment_scores

experiments = load_experiments()

print("\n===== Experiment Score Comparison =====")

compare_experiment_scores(experiments)