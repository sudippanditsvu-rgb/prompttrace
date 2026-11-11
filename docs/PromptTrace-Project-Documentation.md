# PromptTrace — Project Documentation

1. Project Title
2. Introduction
3. Problem Statement
4. Proposed Solution
5. Objectives
6. Target Users
7. Key Features
8. Technology Stack
9. Initial System Architecture
10. Expected Outcome
11. Future Scope

# PromptTrace — Project Documentation

## 1. Project Title

**PromptTrace — A GenAI Prompt Experimentation and Evaluation Assistant**

---

## 2. Introduction

Generative AI tools are becoming useful for learning, development, content creation, research, and many other tasks. However, getting a good result from a Generative AI model often depends on how the prompt is written.

When experimenting with prompts, it can become difficult to remember which prompt version was used, what response was generated, which model was used, and how well the result performed.

PromptTrace is being developed as a lightweight application to make this process more organized.

The main idea of PromptTrace is to allow a user to create prompt experiments, run different prompt versions, save the results, and evaluate or compare them in a structured way.

The project is also being developed as a practical learning project for understanding Python, LLM APIs, prompt engineering, evaluation, data storage, and application development.

---

## 3. Problem Statement

People who regularly experiment with Generative AI prompts may create many versions of the same prompt.

For example, a user may create:

- Prompt v1
- Prompt v2
- Prompt v3
- Prompt v4

and receive different responses from the AI model.

Without a structured system, it can be difficult to keep track of:

- Which prompt produced a particular response
- Which prompt version was used
- Which model generated the response
- How the result was evaluated
- Which prompt performed better

Using simple notes or manually maintaining files can also become difficult as the number of experiments increases.

Therefore, there is a need for a simple system that can organize and evaluate prompt experiments in one place.

---

## 4. Proposed Solution

PromptTrace proposes a lightweight GenAI experimentation assistant where users can create and manage prompt experiments.

The application will allow users to provide a task and prompt, select or use an available LLM, generate a response, and store information about the experiment.

The system will also provide a way to evaluate the generated results and compare different prompt versions.

The initial development is being done using Python and JSON-based storage. As the project develops, the storage system will be improved using SQLite and the application interface will be developed using Streamlit.

---

## 5. Objectives

The main objectives of PromptTrace are:

1. To provide a simple way to create and organize GenAI prompt experiments.

2. To store prompt versions along with their responses and evaluation scores.

3. To make it easier to compare different prompt versions.

4. To understand how changes in prompts can affect AI-generated results.

5. To provide a basic evaluation mechanism for experiment results.

6. To integrate an LLM API into a practical Python application.

7. To provide persistent storage for experiment history.

8. To develop a lightweight and easy-to-use interface for GenAI experimentation.

9. To create a practical project that demonstrates knowledge of Python, Generative AI, prompt engineering, APIs, data storage, and software development.

---

## 6. Target Users

The initial target users of PromptTrace are:

- Students learning Generative AI
- Beginners learning prompt engineering
- Developers experimenting with LLMs
- Learners who want to compare different prompt versions
- Users who want to maintain a record of their GenAI experiments

The project is initially focused on learning and experimentation rather than enterprise-scale usage.

---

## 7. Key Features

The planned core features of PromptTrace include:

### 7.1 Experiment Creation

Users will be able to create an experiment containing information such as:

- Task
- Prompt
- Prompt version
- Model
- AI response
- Score/evaluation

### 7.2 Prompt Version Tracking

Different versions of a prompt can be stored as separate experiments.

For example:

```text
v1 → Initial prompt
v2 → Improved prompt
v3 → More specific prompt
```

This will make it easier to observe how prompt changes affect the output.

### 7.3 LLM Integration

PromptTrace will connect to an LLM through an API.

The initial implementation is planned around a cloud-based LLM API so that large AI models do not need to run locally on the user's computer.

### 7.4 Experiment Storage

Experiments will be stored so that they can be accessed later.

The project currently uses JSON-based storage during development.

SQLite is planned for the more structured database layer as the application develops.

### 7.5 Evaluation

The application will provide a basic evaluation mechanism using scores and evaluation results.

The current prototype uses a simple score-based evaluation:

```text
Score >= 7 → Good Score
Score < 7  → Needs Improvement
```

This evaluation approach is an initial prototype and may be improved later.

### 7.6 Experiment Comparison

A future version of PromptTrace will allow users to compare multiple prompt versions and their results.

---

## 8. Technology Stack

The current planned technology stack is:

| Component | Technology |
|---|---|
| Programming Language | Python |
| Frontend / UI | Streamlit |
| Backend / Application Logic | Python |
| LLM | Gemini API |
| Initial Storage | JSON |
| Database | SQLite |
| Version Control | Git |
| Code Hosting | GitHub |
| Deployment | Streamlit Community Cloud |
| Secrets / API Keys | Environment Variables |

The technology stack may be adjusted during development if a better technical approach is identified.

---

## 9. Initial System Architecture

The initial architecture of PromptTrace is planned as follows:

```text
                    User
                      │
                      ▼
               Streamlit UI
                      │
                      ▼
             Python Application
                      │
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
     Experiment    Evaluation   Storage
      Manager        Logic        Layer
          │                       │
          ▼                       ▼
       LLM API                 SQLite
          │
          ▼
     AI Response
          │
          ▼
       Evaluation
          │
          ▼
      Experiment
        History
```

The architecture is still under development and may change as more components are implemented.

---

## 10. Current Development Status

The project is currently being developed step by step.

The following components have already been practiced or implemented:

- Python fundamentals
- Functions and parameters
- Dictionaries and lists
- Conditional statements
- Loops
- Error handling
- Python modules
- Experiment data structure
- Multiple experiment handling
- Experiment evaluation
- JSON storage
- Saving experiments to a JSON file
- Loading experiments from a JSON file
- Basic Git and GitHub workflow

The current development stage is focused on building the foundation before connecting the application to a real LLM API.

---

## 11. Expected Outcome

The expected outcome of PromptTrace is a working lightweight GenAI experimentation application.

The final application should allow a user to:

```text
Create a Prompt
       ↓
Run the Prompt
       ↓
Receive AI Response
       ↓
Save Experiment
       ↓
Evaluate Result
       ↓
Compare Prompt Versions
       ↓
View Experiment History
```

The project should also demonstrate practical understanding of how a Python application can communicate with an LLM API, process AI responses, store experiment data, and provide a user interface.

---

## 12. Future Scope

Possible future improvements include:

- More advanced prompt evaluation methods
- Automatic evaluation using an LLM
- Better prompt comparison
- Multiple LLM providers
- Experiment filtering and search
- Experiment history dashboard
- Charts for experiment scores
- Exporting experiment results
- More advanced evaluation metrics
- User accounts
- Cloud database support
- Additional AI-assisted experimentation features

These features are considered future possibilities and are not part of the current completed implementation.

---

## 13. Project Development Approach

PromptTrace is being developed incrementally.

Instead of building the complete application at once, each component is being learned, implemented, tested, and then connected with the other components.

The current development approach is:

```text
Learn Concept
     ↓
Practice with Small Code
     ↓
Apply to PromptTrace
     ↓
Test
     ↓
Fix Errors
     ↓
Document Progress
     ↓
Commit to Git
     ↓
Move to Next Component
```

This approach is being used to make sure that the developer understands the project instead of only assembling code from external sources.

---

## 14. Documentation Status

This document is the **initial project documentation**.

It is expected to be updated during development as the actual features, architecture, database design, evaluation methods, and user interface become more clearly defined.

More detailed documents such as the SRS, use case diagram, DFD, ER diagram, testing documentation, and final project report will be prepared in later stages of development.