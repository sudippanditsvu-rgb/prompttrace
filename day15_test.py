from storage import load_experiments
from experiment import find_best_experiment

experiments = load_experiments()

best_experiment = find_best_experiment(experiments)

print("\n===== Best Experiment =====")

if best_experiment is None:
    print("No experiments found.")

else:
    print("Best Prompt Version:", best_experiment["prompt_version"])
    print("Model:", best_experiment["model"])
    print("Score:", best_experiment["score"])