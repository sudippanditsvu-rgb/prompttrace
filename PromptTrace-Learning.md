---

### Day 1

#### What I learned

- Learned about Python variables, lists, and dictionaries.
- Learned how to access values from a dictionary using keys.
- Learned how to use if/else conditions.
- Learned how to use a for loop.
- Understood how a list can contain multiple dictionaries.

#### What I practiced

- Created an experiment dictionary for PromptTrace.
- Stored task, prompt, version, model, response, and score in the dictionary.
- Created multiple experiments and stored them in a list.
- Used if/else to check whether an experiment score was good or needed improvement.
- Used a for loop to process multiple experiments.

#### What I built

- Created a basic experiment evaluation logic.
- Tested multiple experiments with different scores.

#### What I found confusing

- Initially I was confused about how to access values inside a dictionary.
- I also had some confusion about using a for loop with a list of dictionaries.

#### How I solved it

- Practiced dictionary access using examples.
- Used the for loop step by step and checked the value of each experiment.
- Used AI as a mentor when I got stuck and then wrote the code myself.

#### AI help used

- Used AI to understand Python concepts and debug my mistakes.
- I wrote the practice code myself and used AI mainly for explanations and review.

#### What I can explain now

- I can explain the difference between a list and a dictionary.
- I can access dictionary values using keys.
- I can use if/else and for loops with experiment data.
- I can store multiple experiment dictionaries inside a list.

---

### Day 2

#### What I learned

- Learned how to create and use Python functions.
- Learned about function parameters and return values.
- Learned how functions can work with dictionaries and lists.
- Understood why a function returns `None` when it does not return a value.
- Learned how to use `input()` and convert input into an integer.

#### What I practiced

- Created functions for displaying experiment information.
- Created a function to calculate/evaluate scores.
- Created an evaluation function for multiple experiments.
- Used a list to store evaluation results.

#### What I built

- Created a basic PromptTrace experiment evaluation function.
- Tested multiple experiments and returned results such as `Good Score` and `Needs improvement`.

#### What I found confusing

- At first I was confused about the difference between `print()` and `return`.
- I also made a mistake by creating the result list inside the loop, which caused the list to reset.

#### How I solved it

- Practiced how `return` sends a value back from a function.
- Moved the result list outside the loop so all experiment results could be stored.
- Tested the function with two different experiments.

#### AI help used

- Used AI to understand errors and get hints.
- I tried writing the functions myself instead of directly copying the complete solution.

#### What I can explain now

- I can create a function with parameters.
- I understand how `return` works.
- I can use functions with lists and dictionaries.
- I can process multiple experiments using a loop inside a function.

---

### Day 3

#### What I learned

- Learned why data needs to be stored in a file instead of only keeping it in Python memory.
- Learned about JSON and how it can store structured data.
- Learned the difference between `"w"` and `"r"` file modes.
- Learned `json.dump()` and `json.load()`.
- Learned how to save and load a list of dictionaries.

#### What I practiced

- Created an `experiment.json` file.
- Saved PromptTrace experiment data into the JSON file.
- Used `indent=4` to make the JSON file easier to read.
- Loaded the JSON data back into Python.
- Used the loaded data with my experiment evaluation function.

#### What I built

- Created a basic JSON storage system for PromptTrace.
- Saved multiple experiments in `experiment.json`.
- Loaded the experiments again and checked their scores.

#### What I found confusing

- Initially I used `"w"` mode while trying to load the JSON file.
- I was also confused about where `json.dump()` and `json.load()` should be used.

#### How I solved it

- Understood that `"w"` means write and `"r"` means read.
- Learned that `json.dump()` is used for saving Python data to JSON.
- Learned that `json.load()` is used for loading JSON data back into Python.
- Practiced saving and loading the experiments until the output was correct.

#### AI help used

- Used AI to understand JSON concepts and fix mistakes.
- I wrote the code myself and used AI to review my code and explain errors.

#### What I can explain now

- I can explain what JSON is and why it is useful.
- I can save Python dictionaries/lists to a JSON file.
- I can load JSON data back into Python.
- I can use loaded experiment data with functions and loops.
- I understand the basic data flow of PromptTrace storage.

---

## Current Understanding

### PromptTrace Data Flow

User creates experiment  
↓  
Python stores experiment data  
↓  
Experiments are saved in JSON  
↓  
JSON data can be loaded again  
↓  
Python evaluates the experiments  
↓  
Results can be compared

### My Current Skills

- Python basics
- Lists
- Dictionaries
- If/else
- For loops
- Functions
- Parameters
- Return values
- File handling basics
- JSON
- `json.dump()`
- `json.load()`
- Basic experiment evaluation
- Git and GitHub basics

### Things I Still Need to Learn

- Error handling
- Working with APIs
- Calling an LLM API
- Prompt version management
- Better evaluation methods
- Streamlit UI
- SQLite/database basics
- Connecting all components into the final PromptTrace application

### Current Feeling About the Project

At the beginning, the project structure was confusing to me because I was still learning Python. After practicing step by step, I understand the basic flow much better. I am still not fully confident with Python, but now I can write small parts of the project myself and understand what the code is doing.

---