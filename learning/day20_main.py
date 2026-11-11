from storage import load_experiments
from experiment import rank_experiments, evaluate_experiments

experiments = load_experiments()

ranked_experiments = rank_experiments(experiments)

evaluations = evaluate_experiments(ranked_experiments)

print("\n===== Experiment Ranking Details =====")

for experiment, evaluation in zip(ranked_experiments, evaluations):

    print("\nPrompt Version:", experiment["prompt_version"])
    print("Model:", experiment["model"])
    print("Score:", experiment["score"])
    print("Evaluation:", evaluation)