words = ["apple", "banana", "apple", "cherry", "banana", "apple", "orange"]

word_counts = {}

for w in words:
    word_counts[w] = word_counts.get(w, 0) + 1

print("Word Counts: ", word_counts)

items_more_than_once = [key for key, value in word_counts.items() if value > 1 ]

print("Word Counts: ", items_more_than_once)