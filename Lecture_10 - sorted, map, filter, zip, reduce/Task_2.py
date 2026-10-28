scores = [45, 82, 67, 38, 90, 55, 72]
print("scores: ", scores, "\n")

passed_scores = list(filter(lambda x: x >= 50, scores))
print("Passed scores: ", passed_scores, "\n")

passed_scores_with_bonus = list(map(lambda x: x + 5 if x <=95 else 100, passed_scores))
print("Passed scores with bonus: ", passed_scores_with_bonus, "\n")