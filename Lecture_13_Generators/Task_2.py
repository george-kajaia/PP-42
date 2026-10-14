words = ["python", "generator", "yield", "code", "ai", "developer"]

words_filterer = (x for x in words if len(x) > 4)

func = words_filterer

for x in func:
    print(x)