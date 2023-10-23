# 2
def occurrences(sir):
    dictionar = dict()
    for ch in sir:
        if ch in dictionar.keys():
            dictionar[ch] += 1
        else:
            dictionar[ch] = 1
    return dictionar


print(occurrences("Ana has apples."))
