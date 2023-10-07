# 1
def gcd(n):
    List = []
    c = 1
    while n:
        List.append(input())
        n = n - 1
    for i in range(2, int(min(List)) + 1):
        ok = 1
        for x in List:
            if int(x) % i != 0:
                ok = 0
                break
        if ok == 1:
            c = c * i
    print(c)


gcd(5)
