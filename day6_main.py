
from experiment import evaluate_experiments, create_experiment
from storage import save_experiments, load_experiments
from llm import generate_response


# Create prompt
prompt = "Explain Generative AI in simple words."


# Generate actual AI response
try:
    response = generate_response(prompt)

    print("\nGemini Response:")
    print(response)

except Exception as e:
    print("\nFailed to generate response:")
    print(e)

    raise


# Create experiment
experiment1 = create_experiment(
    "Gen AI",
    prompt,
    "v1",
    "Gemini",
    response,
    9
)


# Store experiment
experiments = [experiment1]

save_experiments(experiments)

print("\nExperiment saved successfully!")


# Load experiments
loaded_experiments = load_experiments()


# Evaluate experiments
result = evaluate_experiments(loaded_experiments)

print("\nEvaluation Results:")
print(result)
