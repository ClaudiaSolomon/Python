# 1
def list_sets(list1, list2):
    list3 = set(list1).union(list2)
    list4 = set(list1).intersection(list2)
    list5 = set(list1).difference(list2)
    list6 = set(list2).difference(list1)
    return [list3, list4, list5, list6]


print(list_sets([1, 2, 3, 4], [1, 2, 10, 9]))
