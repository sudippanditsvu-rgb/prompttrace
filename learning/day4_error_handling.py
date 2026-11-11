#value error handling
"""try:
    score=int(input("Enter the score: "))
    print(score)
except ValueError:
    print("Please enter a valid number.")
"""
#value error handling
"""
import json


experiment = {
    "task": "Gen AI",
    "score": "9"
}

def safe_score(score):
    try:

        score = int(score)
        print(score)
        
        
    except ValueError:
        
        print("Please enter a valid number.")
        
safe_score(experiment["score"])


with open("experiment.json", "w") as f:
    json.dump(experiment, f, indent=4)
"""
###Key Error Handling
"""experiment = {
    "task": "Gen AI",
    
}
def show_error():
    try:
        print(experiment["score"])
    except KeyError:
        print("Score key not found in experiment.")
show_error()"""

#key error and value error handling
experiment={
    "task":"Gen Ai",
    "prompt":"explain me the concept of gen ai",
    "prompt_version":"v1",
    "model":"LLM",
    "response":".....",
    
}

def safe_experiment_score():
    try:
        print(experiment["score"])
        
        print(score)
    except KeyError:
        print("Score key not found in experiment.")
    except ValueError:
        print("Please enter a valid number.")
safe_experiment_score()