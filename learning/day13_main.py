from storage import load_experiments
from experiment import calculate_statistics

experiments = load_experiments()

statistics = calculate_statistics(experiments)

print("\n===== PromptTrace Statistics =====")

print("Total Experiments:", statistics["total"])

print("Average Score:", statistics["average"])

print("Highest Score:", statistics["highest"])

print("Lowest Score:", statistics["lowest"])