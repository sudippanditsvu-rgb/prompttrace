"""def create_experiment():
    experiment={
        "task": "Gen AI",
        "prompt": "explain me the concept of gen ai",
        "prompt_version": "v1",
        "model": "LLM",
        "response": ".....",
        "score": 9
    }
    return experiment

my_experiment = create_experiment()
print(my_experiment)"""
#call two input parameters to the function
"""def create_experiment(task,model):
    experiment={
        "task":task,
        "model":model
    }
    return experiment
result=create_experiment("Gen AI","LLM")
print(result)"""
#call 6 input in dictinary
"""def create_experiment(task, prompt, prompt_version, model, response, score):
    experiment={
        "task": task,
        "prompt": prompt,
        "prompt_version": prompt_version,
        "model": model,
        "response": response,
        "score": score
    }
    return experiment
result=create_experiment("Gen AI", "explain me the concept of gen ai", "v1", "LLM", ".....", 9)
print(result)"""

"""def create_experiment(task, prompt, prompt_version, model, response, score):
    experiment={
        "task": task,
        "prompt": prompt,
        "prompt_version": prompt_version,
        "model": model,
        "response": response,
        "score": score
    }
    return experiment
experiment1=create_experiment("Gen AI", "explain me the concept of gen ai", "v1", "LLM", ".....", 9)
experiment2=create_experiment("Gen AI", "explain me the concept of gen ai", "v1", "LLM", ".....", 8)
print(experiment1)
print(experiment2)"""

"""def create_experiment(task, prompt, prompt_version, model, response, score):
    experiment={
        "task": task,
        "prompt": prompt,
        "prompt_version": prompt_version,
        "model": model,
        "response": response,
        "score": score
    }
    return experiment
experiment1=create_experiment("Gen AI", "explain me the concept of gen ai", "v1", "LLM", ".....", 9)
experiment2=create_experiment("Gen AI", "explain me the concept of gen ai", "v1", "LLM", ".....", 8)
experiments=[experiment1,experiment2]
print(experiments)
print(len(experiments))""

experiment1 = {
    "task": "Gen AI",
    "prompt": "explain me the concept of gen ai",
    "prompt_version": "v1",
    "model": "LLM",
    "response": ".....",
    "score": 9
}
experiment2 = {
    "task": "Gen AI",
    "prompt": "explain me the concept of gen ai",
    "prompt_version": "v1",
    "model": "LLM",
    "response": ".....",
    "score": 2
}
experiments = [experiment1, experiment2]
def create_experiments(experiments):
    for i in experiments:
        if (i["score"]>=7):
            print("Good Score")
        else:
            print("Needs Improvement")
create_experiments(experiments)



experiment1 = {
    "task": "Gen AI",
    "prompt": "explain me the concept of gen ai",
    "prompt_version": "v1",
    "model": "LLM",
    "response": ".....",
    "score": 9
}
experiment2 = {
    "task": "Gen AI",
    "prompt": "explain me the concept of gen ai",
    "prompt_version": "v1",
    "model": "LLM",
    "response": ".....",
    "score": 9
}
experiments = [experiment1, experiment2]
def evaluate_experiments(experiments):
    results = []
    for i in experiments:
        if (i["score"]>=7):
            results.append("Good score")
        else:
            results.append("Needs Improvement")
    return results
results =evaluate_experiments(experiments)
print(results)
"""

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