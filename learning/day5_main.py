"""from score_utils import calculate_score"""
from score_utils import evaluate_score, get_score_message

"""calculated_score = calculate_score(9)"""
calculated_score = evaluate_score(5)

result = evaluate_score(2)
message = get_score_message(9)
print(result)
print(message)