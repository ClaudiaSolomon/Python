# 4
def music(list1, list2, n):
    list_final = [list1[n]]
    for x in list2:
        n = n + x
        if n < 0:
            n = len(list1) + n
        if n > len(list1):
            n = n - len(list1)
        list_final.append(list1[n])
    return list_final


print(music(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
