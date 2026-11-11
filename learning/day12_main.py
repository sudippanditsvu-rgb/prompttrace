from storage import load_experiments
from experiment import show_experiment_history


experiments = load_experiments()

show_experiment_history(experiments)