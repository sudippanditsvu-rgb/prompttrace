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