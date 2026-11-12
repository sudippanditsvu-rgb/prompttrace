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


def calculate_statistics(experiments):

    total_experiments = len(experiments)

    if total_experiments == 0:
        return {
            "total": 0,
            "average": 0,
            "highest": 0,
            "lowest": 0
        }

    total_score = 0

    for experiment in experiments:
        total_score += experiment["score"]

    average_score = total_score / total_experiments

    highest_score = max(
        experiment["score"] for experiment in experiments
    )

    lowest_score = min(
        experiment["score"] for experiment in experiments
    )

    return {
        "total": total_experiments,
        "average": round(average_score, 2),
        "highest": highest_score,
        "lowest": lowest_score
    }

def find_best_experiment(experiments):

    if len(experiments) == 0:
        return None

    best_experiment = experiments[0]

    for experiment in experiments:
        if experiment["score"] > best_experiment["score"]:
            best_experiment = experiment

    return best_experiment

def find_second_best_experiment(experiments):

    if len(experiments) < 2:
        return None

    ranked_experiments = sorted(
        experiments,
        key=lambda experiment: experiment["score"],
        reverse=True
    )

    return ranked_experiments[1]

def compare_experiment_scores(experiments):

    for experiment in experiments:
        print(
            experiment["prompt_version"],
            ":",
            experiment["score"]
        )

def rank_experiments(experiments):

    if len(experiments) == 0:
        return []

    ranked_experiments = sorted(
        experiments,
        key=lambda experiment: experiment["score"],
        reverse=True
    )

    return ranked_experiments