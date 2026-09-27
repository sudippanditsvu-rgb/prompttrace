"""try:
    score=int(input("Enter the score: "))
    print(score)
except ValueError:
    print("Please enter a valid number.")
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
        
        # yahan score ko int mein convert karna hai
    except ValueError:
        
        print("Please enter a valid number.")
        
safe_score(experiment["score"])


with open("experiment.json", "w") as f:
    json.dump(experiment, f, indent=4)

