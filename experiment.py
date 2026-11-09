def create_experiment(task, prompt, prompt_version, model, response, score):
    experiment = {
        "task": task,
        "prompt": prompt,
        "prompt_version": prompt_version,
        "model": model,
        "response": response,
        "score": score
    }

    return experiment


def evaluate_experiments(experiments):
    results = []

    for i in experiments:
        if i["score"] >= 7:
            results.append("Good Score")
        else:
            results.append("Needs Improvement")

    return results


def show_experiment_history(experiments):
    results = evaluate_experiments(experiments)

    print("\n===== PromptTrace Experiment History =====")

    print("Total experiments:", len(experiments))

    for i, experiment in enumerate(experiments):

        print("\nExperiment", i + 1)

        print("Prompt Version:", experiment["prompt_version"])

        print("Model:", experiment["model"])

        print("Score:", experiment["score"])

        print("Prompt:", experiment["prompt"])

        print("Evaluation:", results[i])

        response = experiment["response"]

        print("Response:", response[:300])

        if len(response) > 300:
            print("... (Response shortened)")

    good_score = results.count("Good Score")

    needs_improvement = results.count("Needs Improvement")

    print("\n===== Experiment Summary =====")

    print("Good Score:", good_score)

    print("Needs Improvement:", needs_improvement)