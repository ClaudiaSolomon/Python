# 6
def lists(n, *argv):
    list_oc = []
    list_final = []
    for arg in argv:
        for x in arg:
            list_oc.append(x)
    print(list_oc)
    for x in list_oc:
        if list_oc.count(x) == n:
            list_final.append(x)
    list_no_duplicates = list(set(list_final))
    return list_no_duplicates


print(lists(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))
