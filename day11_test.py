from storage import save_experiments, load_experiments

print("Before test:")

experiments = load_experiments()

print("Total experiments:", len(experiments))

test_experiment = {
    "task": "Duplicate Test",
    "prompt": "Test duplicate prevention",
    "prompt_version": "v3",
    "model": "Test",
    "response": "Testing duplicate prevention",
    "score": 5
}

save_experiments([test_experiment])

print("\nAfter test:")

experiments = load_experiments()

print("Total experiments:", len(experiments))

for experiment in experiments:
    print(
        experiment["prompt_version"],
        experiment["score"]
    )