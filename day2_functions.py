"""def myfunction():
    print("Welcome to PromptTrace")
myfunction()"""
"""def show_task(task):
    print(f"{task}: Generative AI")
show_task("Task")"""
"""def show_task(task1, task2):
    print(f"{task1}: Generative AI")
    print(f"{task2}: Prompt Engineering")
show_task("Task 1", "Task 2")
def show_task(task1, task2):
    print(f"Task: {task1}")
    print(f"Task: {task2}")
show_task("Generative AI", "Prompt Engineering")"""

"""def show_experiment(experiment):
    print("Task:",experiment["task"])
    print("Version:",experiment["prompt_version"])
    print("Score:",experiment["score"])

show_experiment(experiment)"""
"""def calculate_score(score):
    return score
score=calculate_score(10)
print(score)"""
"""def ifelse(score):
    if score>=7:
        return "Good Score"
    else:
        return "Needs improvement"
score = int(input("Enter the score: "))
print(ifelse(score))"""

"""def evaluate_experiment(experiment):
    if experiment["score"] >= 7:
        return "Good Score"
    else:
        return "Needs improvement"
result = evaluate_experiment(experiment1)
print(result)"""

experiment1={
    "task":"Gen Ai",
    "prompt":"explain me the concept of gen ai",
    "prompt_version":"v1",
    "model":"LLM",
    "response":".....",
    "score":9
}
experiment2={
    "task":"Gen Ai",
    "prompt":"explain me the concept of gen ai",
    "prompt_version":"v1",
    "model":"LLM",
    "response":".....",
    "score":5
}
experiments=[experiment1, experiment2]

def evaluate_experiment(experiments):
    for i in experiments:
        if i["score"] >=7:
            print("Good Score")
        else:
            print("Needs improvement")
result=evaluate_experiment(experiments)
print(result)

