# 10
def order_lists(*argv):
    max_length = 0
    list_tuples = []
    for arg in argv:
        if len(arg) > max_length:
            max_length = len(arg)
    for i in range(max_length):
        tuple_p = ()
        for arg in argv:
            if len(arg) <= i:
                tuple_p += (None,)
            else:
                tuple_p += (arg[i],)
        list_tuples.append(tuple_p)
    return list_tuples


print(order_lists([1, 2, 3], [5, 6, 7], ["a", "b", "c", "d"]))
