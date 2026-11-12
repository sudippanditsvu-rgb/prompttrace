scores = [10, 10, 8, 8, 5]

previous_score = None
current_rank = 0

for position, score in enumerate(scores, start=1):

    if score != previous_score:
        current_rank = position

    print("Rank:", current_rank, "Score:", score)

    previous_score = score