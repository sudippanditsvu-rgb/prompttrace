"""project_name="PromptTrace"
project_type="Generative AI"
developer="Sudip Pandit"
prompt_version="v1"


#dictonary
experiment={
    "project_type": "Experimental Generative AI",
    "prompt_version": "v1",
    "developer": "Sudip Pandit"
}
print(experiment)

print("Project: ",project_name)
print("Project Type: ",project_type)
print("Developer: ",developer)
print("Prompt Version: ",prompt_version)

print(experiment["project_type"])
print(experiment["developer"])

experiment1={
    "task":"Gen Ai",
    "prompt":"explain me the concept of gen ai",
    "prompt_version":"v1",
    "model":"LLM",
    "response":".....",
    "score":10
}

prompt_versions=["v1","v2","v3","v4"]

print(experiment1)
print(experiment1["task"])
print(experiment1["prompt"])
print(experiment1["score"])

print(prompt_versions[0])
print(prompt_versions[1])
print(prompt_versions[2])
print(prompt_versions[3])

#if else statement
score=10
if score>=7:
    print("Good Score")
else:
    print("Needs improvement")

"""
#loops
prompt_versions=["v1","v2","v3","v4"]
for i in prompt_versions:
    print(i)
