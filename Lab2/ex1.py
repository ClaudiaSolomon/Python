# 1
def fibonacci(n):
    List = []
    t1 = 0
    t2 = 1
    List.append(t1)
    List.append(t2)
    for i in range(2, n):
        t3 = t1 + t2
        List.append(t3)
        t1 = t2
        t2 = t3
    return List


print(fibonacci(9))
