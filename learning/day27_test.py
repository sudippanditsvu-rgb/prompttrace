
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from experiment import (
    validate_experiment_details,
    validate_score
)


print("\n===== Day 27 Backend Validation Tests =====")


# Test 1: Valid experiment details

result = validate_experiment_details(
    "GenAI Testing",
    "Explain Generative AI",
    "v6"
)

assert result is None

print("Test 1 Passed: Valid experiment details")


# Test 2: Empty task

result = validate_experiment_details(
    "",
    "Explain AI",
    "v6"
)

assert result is not None

print("Test 2 Passed: Empty task rejected")


# Test 3: Empty prompt

result = validate_experiment_details(
    "AI Testing",
    "",
    "v6"
)

assert result is not None

print("Test 3 Passed: Empty prompt rejected")


# Test 4: Empty version

result = validate_experiment_details(
    "AI Testing",
    "Explain AI",
    ""
)

assert result is not None

print("Test 4 Passed: Empty version rejected")


# Test 5: Valid score

result = validate_score(8)

assert result is None

print("Test 5 Passed: Valid score accepted")


# Test 6: Score below 1

result = validate_score(0)

assert result is not None

print("Test 6 Passed: Invalid low score rejected")


# Test 7: Score above 10

result = validate_score(11)

assert result is not None

print("Test 7 Passed: Invalid high score rejected")


# Test 8: Invalid score type

result = validate_score("hello")

assert result is not None

print("Test 8 Passed: Invalid score type rejected")


print("\nAll Day 27 Validation Tests Passed!")
