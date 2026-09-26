scores = []

scores.append(45)
scores.append(88)
scores.append(92)
scores.append(60)
scores.append(75)

print("scores")
print(scores, "\n")

scores.remove(45)
print("remove the element 45")
print(scores, "\n")

avg = sum(scores) / len(scores)
print(f"The avg. value is: {avg}", "\n")

print(f"The max. value is: {max(scores)}", "\n")
print(f"The min. value is: {min(scores)}", "\n")

# ----Min-Max-ის მეორე ვერსია----
# scores.sort()
# print(f"The max value is: {scores[-1]}", "\n")
# print(f"The min value is: {scores[0]}", "\n")

scores.sort()
print("Sorted (ascending) list")
print(scores, "\n")

passed_scores = []
for x in scores:
    if x >= 60:
        passed_scores.append(x)

print("passed scores (>= 60) ")
print(passed_scores)