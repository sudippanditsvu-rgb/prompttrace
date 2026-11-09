from storage import load_experiments

experiments = load_experiments()

print("\n===== PromptTrace Statistics =====")

print("Total Experiments:", len(experiments))

#average score
total_score = 0

for experiment in experiments:
    total_score += experiment["score"]

average_score = total_score / len(experiments)

print("Average Score:", round(average_score, 2))

#higest score
highest_score = 0

for experiment in experiments:
    if experiment["score"] > highest_score:
        highest_score = experiment["score"]

print("Highest Score:", highest_score)

#lowest score 

lowest_score = 10

for experiment in experiments:
    if experiment["score"] < lowest_score:
        lowest_score = experiment["score"]

print("Lowest Score:", lowest_score)