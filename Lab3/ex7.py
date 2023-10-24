# 7
def set_operations(*sets):
    dictionar = dict()
    for i in range(0, len(sets)):
        for j in range(i + 1, len(sets)):
            dictionar[str(sets[i]) + " | " + str(sets[j])] = sets[i].union(sets[j])
            dictionar[str(sets[i]) + " & " + str(sets[j])] = sets[i].intersection(sets[j])
            dictionar[str(sets[i]) + " - " + str(sets[j])] = sets[i].difference(sets[j])
            dictionar[str(sets[j]) + " - " + str(sets[i])] = sets[j].difference(sets[i])
    return dictionar


print(set_operations({1, 2}, {2, 3}, {3}))
