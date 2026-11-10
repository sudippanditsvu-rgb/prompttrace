from experiment import calculate_statistics

experiments = []

statistics = calculate_statistics(experiments)

print("\n===== Empty Experiment Test =====")

print("Total:", statistics["total"])
print("Average:", statistics["average"])
print("Highest:", statistics["highest"])
print("Lowest:", statistics["lowest"])