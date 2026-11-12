
import sys
from pathlib import Path
from datetime import datetime

sys.path.append(str(Path(__file__).resolve().parent.parent))

from database import (
    create_table,
    insert_experiment,
    fetch_all_experiments,
    delete_experiment_from_db
)


print("\n===== Day 28 SQLite Database Tests =====")

create_table()

test_experiment = {
    "task": "Database Testing",
    "prompt": "Test SQLite database",
    "prompt_version": "day28_test_temp",
    "model": "Gemini",
    "response": "Database test successful",
    "score": 8,
    "created_at": datetime.now().isoformat(timespec="seconds")
}


# Test 1: Insert record

result = insert_experiment(test_experiment)

assert result is True

print("Test 1 Passed: Experiment inserted")


# Test 2: Fetch record

experiments = fetch_all_experiments()

found = any(
    e["prompt_version"] == "day28_test_temp"
    for e in experiments
)

assert found is True

print("Test 2 Passed: Experiment fetched")


# Test 3: Duplicate prevention

result = insert_experiment(test_experiment)

assert result is False

print("Test 3 Passed: Duplicate rejected")


# Test 4: Delete record

result = delete_experiment_from_db("day28_test_temp")

assert result is True

print("Test 4 Passed: Experiment deleted")


# Test 5: Confirm deletion

experiments = fetch_all_experiments()

found = any(
    e["prompt_version"] == "day28_test_temp"
    for e in experiments
)

assert found is False

print("Test 5 Passed: Deleted record not found")


print("\nAll Day 28 Database Tests Passed!")
