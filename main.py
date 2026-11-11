
from storage import load_experiments
from experiment import (
    rank_experiments,
    evaluate_experiments,
    calculate_statistics,
    find_best_experiment
)


def main():
    experiments = load_experiments()

    if not experiments:
        print("No experiments found.")
        return

    ranked_experiments = rank_experiments(experiments)
    evaluations = evaluate_experiments(ranked_experiments)

    print("\n===== PromptTrace Dashboard =====")
    print("Total Experiments:", len(experiments))

    print("\n===== Experiment Rankings =====")

    for experiment, evaluation in zip(ranked_experiments, evaluations):
        print("\nPrompt Version:", experiment["prompt_version"])
        print("Model:", experiment["model"])
        print("Score:", experiment["score"])
        print("Evaluation:", evaluation)

    statistics = calculate_statistics(experiments)

    print("\n===== PromptTrace Statistics =====")
    print("Total:", statistics["total"])
    print("Average Score:", statistics["average"])
    print("Highest Score:", statistics["highest"])
    print("Lowest Score:", statistics["lowest"])

    best_experiment = find_best_experiment(experiments)

    print("\n===== Best Experiment =====")
    print("Prompt Version:", best_experiment["prompt_version"])
    print("Model:", best_experiment["model"])
    print("Score:", best_experiment["score"])


if __name__ == "__main__":
    main()
