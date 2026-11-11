
from storage import load_experiments, save_experiments
from experiment import (
    create_experiment,
    rank_experiments,
    evaluate_experiments,
    calculate_statistics,
    find_best_experiment
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

    for rank, (experiment, evaluation) in enumerate(zip(ranked_experiments, evaluations), start=1):
        print(f"\nRank {rank}")
        print("Prompt Version:", experiment["prompt_version"])
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

    print("\n===== Welcome to PromptTrace =====")
    print("1. View Experiment Dashboard")
    print("2. Create New Experiment")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        main()

    elif choice == "2":
        run_new_experiment()

    elif choice == "3":
        print("Thank you for using PromptTrace!")

    else:
        print("Invalid choice. Please select 1, 2, or 3.")