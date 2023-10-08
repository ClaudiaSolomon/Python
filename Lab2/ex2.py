# 2
def prime(List):
    List_prime = []
    for x in List:
        ok = 1
        for i in range(2, x):
            if x % i == 0:
                ok = 0
                break
        if ok == 1:
            List_prime.append(x)
    return List_prime


print(prime([1, 2, 6, 7, 3, 19]))
