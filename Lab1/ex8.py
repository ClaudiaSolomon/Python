# 8
def binary(n):
    count = 0
    while n:
        if n % 2 == 1:
            count = count + 1
        n = int(n / 2)
    print(count)


binary(24)
