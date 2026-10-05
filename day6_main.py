
from experiment import evaluate_experiments,create_experiment

experiment1 = create_experiment(
    "Gen AI",
    "explain me the concept of gen ai",
    "v1",
    "LLM",
    ".....",
    9
)

experiment2 = create_experiment(
    "Gen AI",
    "explain me the concept of gen ai",
    "v2",
    "LLM",
    ".....",
    2
)

experiments = [experiment1, experiment2]

results = evaluate_experiments(experiments)

print(results)