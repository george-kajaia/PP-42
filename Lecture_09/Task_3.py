def analyze_text(text, min_length=3, ignore_stopwords=None):
    if ignore_stopwords is None:
        ignore_stopwords = set()

    return set(x for x in text.split() if len(x) >= min_length) - ignore_stopwords


str = analyze_text("giorgi dato ia ana nino")
print(str, "\n")

str = analyze_text("giorgi dato ia ana nino", ignore_stopwords = {"giorgi"})
print(str, "\n")

str = analyze_text(text = "giorgi dato ia ana nino", min_length = 4)
print(str, "\n")

str = analyze_text(text = "giorgi dato ia ana nino", min_length = 4, ignore_stopwords = {"giorgi"})
print(str, "\n")

