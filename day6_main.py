
from experiment import evaluate_experiments, create_experiment
from storage import save_experiments, load_experiments


# Temporary responses for testing
response_v1 = "Generative AI creates new content using learned patterns."
response_v2 = "Generative AI can create text, images, and other content."


# Create experiments
experiment1 = create_experiment(
    "Gen AI",
    "Explain Generative AI in simple words.",
    "v1",
    "Gemini",
    response_v1,
    9
)

experiment2 = create_experiment(
    "Gen AI",
    "Explain Generative AI with an example.",
    "v2",
    "Gemini",
    response_v2,
    2
)


# Store experiments
experiments = [experiment1, experiment2]

save_experiments(experiments)

print("Experiments saved successfully!")


# Load experiments
loaded_experiments = load_experiments()


# Evaluate experiments
result = evaluate_experiments(loaded_experiments)

print("\nEvaluation Results:")
print(result)
