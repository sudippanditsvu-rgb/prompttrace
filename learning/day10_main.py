
from llm import generate_response
from experiment import create_experiment, evaluate_experiments
from storage import save_experiments, load_experiments

task = "Explain Generative AI"

prompt_v1 = "Explain Generative AI."

prompt_v2 = "Explain Generative AI in simple words with one real-life example for a beginner."

print("Generating response for Prompt v1...")
response_v1 = generate_response(prompt_v1)

print("\nGenerating response for Prompt v2...")
response_v2 = generate_response(prompt_v2)

experiment1 = create_experiment(
    task,
    prompt_v1,
    "v1",
    "Gemini",
    response_v1,
    6
)

experiment2 = create_experiment(
    task,
    prompt_v2,
    "v2",
    "Gemini",
    response_v2,
    9
)

experiments = [experiment1, experiment2]

save_experiments(experiments)

print("\nBoth experiments saved!")

loaded_experiments = load_experiments()


print("\nEvaluation Results:")

results = evaluate_experiments(loaded_experiments)

for experiment, result in zip(loaded_experiments, results):
    print(
        experiment["prompt_version"],
        "Score:",
        experiment["score"],
        "Result:",
        result
    )




print("\nPrompt Comparison:")

for experiment in loaded_experiments:
    print("\nPrompt Version:", experiment["prompt_version"])
    print("Prompt:", experiment["prompt"])
    print("Response:", experiment["response"])
