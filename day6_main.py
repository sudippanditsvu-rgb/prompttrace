
from experiment import evaluate_experiments,create_experiment

from storage import save_experiments,load_experiments

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

"""results = evaluate_experiments(experiments)"""

"""print(results)"""

save_experiments(experiments)

loaded_experiments = load_experiments()

result = evaluate_experiments(loaded_experiments)
print(result)

