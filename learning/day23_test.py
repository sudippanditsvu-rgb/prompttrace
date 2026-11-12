import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from experiment import find_second_best_experiment

scores = [10, 9, 9, 6, 5]

ranked_scores = sorted(scores, reverse=True)

best_score = ranked_scores[0]
second_best_score = ranked_scores[1]

difference = best_score - second_best_score

print("Best Score:", best_score)
print("Second-Best Score:", second_best_score)
print("Score Difference:", difference)




experiments = [
    {"prompt_version": "v1", "score": 10},
    {"prompt_version": "v2", "score": 9},
    {"prompt_version": "v3", "score": 7},
    {"prompt_version": "v4", "score": 5}
]

second_best = find_second_best_experiment(experiments)

print("\n===== Second-Best Experiment =====")

print("Prompt Version:", second_best["prompt_version"])
print("Score:", second_best["score"])

print("\n===== Edge Case Testing =====")

print("Empty List:", find_second_best_experiment([]))

single_experiment = [
    {"prompt_version": "v1", "score": 10}
]

print(
    "Single Experiment:",
    find_second_best_experiment(single_experiment)
)

print("\n===== Tie Position Test =====")

test_experiments = [
    {"prompt_version": "v1", "score": 10},
    {"prompt_version": "v2", "score": 10},
    {"prompt_version": "v3", "score": 8},
    {"prompt_version": "v4", "score": 8},
    {"prompt_version": "v5", "score": 5}
]

second_best = find_second_best_experiment(test_experiments)

print("Second Position:", second_best["prompt_version"])
print("Second Position Score:", second_best["score"])

score_difference = (
    test_experiments[0]["score"] - second_best["score"]
)

print("Score Difference:", score_difference)