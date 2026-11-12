
from storage import load_experiments, save_experiments, update_experiments

from experiment import (
    create_experiment,
    rank_experiments,
    evaluate_experiments,
    calculate_statistics,
    find_best_experiment,
    find_second_best_experiment,
    find_experiment_by_version,
    filter_experiments_by_evaluation,
    delete_experiment_by_version
)

from llm import generate_response





def run_new_experiment():
    print("\n===== Create New Experiment =====")

    task = input("Enter task name: ")
    prompt = input("Enter your prompt: ")
    prompt_version = input("Enter prompt version (e.g. v5): ")

    experiments = load_experiments()

    # Check duplicate prompt version
    for experiment in experiments:
        if experiment["prompt_version"] == prompt_version:
            print("This prompt version already exists!")
            return

    # Generate response only once
    print("\nGenerating Gemini response...")

    response = generate_response(prompt)

    print("\n===== Gemini Response =====")
    print(response)

    # Rate the generated response
    try:
        score = int(input("\nRate this response (1-10): "))

        if score < 1 or score > 10:
            print("Score must be between 1 and 10.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    new_experiment = create_experiment(
        task,
        prompt,
        prompt_version,
        "Gemini",
        response,
        score
    )

    save_experiments([new_experiment])

    print("\n===== Experiment Saved =====")
    print("Prompt Version:", prompt_version)
    print("Model: Gemini")
    print("Score:", score)
    print("Evaluation:", "Good Score" if score >= 7 else "Needs Improvement")


def search_experiment():

    print("\n===== Experiment Search =====")

    prompt_version = input("Enter Prompt Version: ")

    experiments = load_experiments()

    result = find_experiment_by_version(
        experiments,
        prompt_version
    )

    if result is not None:

        print("\n===== Search Result =====")
        print("Prompt Version:", result["prompt_version"])
        print("Model:", result["model"])
        print("Score:", result["score"])
        print(
            "Evaluation:",
            "Good Score" if result["score"] >= 7
            else "Needs Improvement"
        )

    else:
        print("\nExperiment Not Found!")


def filter_experiments():

    print("\n===== Filter Experiments =====")
    print("1. Good Score")
    print("2. Needs Improvement")

    choice = input("\nSelect filter: ")

    if choice == "1":
        evaluation = "Good Score"

    elif choice == "2":
        evaluation = "Needs Improvement"

    else:
        print("Invalid choice!")
        return

    experiments = load_experiments()

    filtered_experiments = filter_experiments_by_evaluation(
        experiments,
        evaluation
    )

    print("\n===== Filter Results =====")

    if len(filtered_experiments) == 0:
        print("No experiments found!")
        return

    for experiment in filtered_experiments:
        print("\nPrompt Version:", experiment["prompt_version"])
        print("Model:", experiment["model"])
        print("Score:", experiment["score"])
        print("Evaluation:", evaluation)

def delete_experiment():

    print("\n===== Delete Experiment =====")

    prompt_version = input("Enter Prompt Version: ")

    experiments = load_experiments()

    result = delete_experiment_by_version(
        experiments,
        prompt_version
    )

    if result:

        confirmation = input(
            "Are you sure you want to delete this experiment? (yes/no): "
        )

        if confirmation.lower() == "yes":

            update_experiments(experiments)

            print("\nExperiment", prompt_version, "deleted successfully!")

        else:
            print("\nDeletion cancelled!")

    else:
        print("\nExperiment Not Found!")


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

    previous_score = None
    current_rank = 0

    for position, (experiment, evaluation) in enumerate(
        zip(ranked_experiments, evaluations), start=1
    ):

        score = experiment["score"]

        if score != previous_score:
            current_rank = position

        print(f"\nRank {current_rank}")
        print("Prompt Version:", experiment["prompt_version"])
        print("Model:", experiment["model"])
        print("Score:", score)
        print("Evaluation:", evaluation)

        previous_score = score

    statistics = calculate_statistics(experiments)

    print("\n===== PromptTrace Statistics =====")
    print("Total:", statistics["total"])
    print("Average Score:", statistics["average"])
    print("Highest Score:", statistics["highest"])
    print("Lowest Score:", statistics["lowest"])

    best_experiment = find_best_experiment(experiments)

    second_best_experiment = find_second_best_experiment(experiments)

    print("\n===== Best Experiment =====")
    print("Prompt Version:", best_experiment["prompt_version"])
    print("Model:", best_experiment["model"])
    print("Score:", best_experiment["score"])

    if second_best_experiment is not None:

        score_difference = (
            best_experiment["score"] - second_best_experiment["score"]
        )

        print("\n===== Second-Best Experiment =====")
        print("Prompt Version:", second_best_experiment["prompt_version"])
        print("Model:", second_best_experiment["model"])
        print("Score:", second_best_experiment["score"])

        print("\n===== Experiment Comparison =====")
        print("Score Difference:", score_difference)

    else:
        print("\nSecond-Best Experiment: Not Available")

if __name__ == "__main__":

    print("\n===== Welcome to PromptTrace =====")
    print("1. View Experiment Dashboard")
    print("2. Create New Experiment")
    print("3. Search Experiment")
    print("4. Filter Experiments")
    print("5. Delete Experiment")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        main()

    elif choice == "2":
        run_new_experiment()

    elif choice == "3":
        search_experiment()

    elif choice == "4":
        filter_experiments()

    elif choice == "5":
        delete_experiment()

    elif choice == "6":
        print("Thank you for using PromptTrace!")

    else:
        print("Invalid choice. Please select 1, 2, 3, 4, 5, or 6.")