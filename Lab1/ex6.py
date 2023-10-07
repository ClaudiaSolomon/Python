# 6
def palindrome(x):
    n = x
    m = x
    p = 0
    count = 1
    while n != 0:
        count = count * 10
        n = int(n / 10)
    count = int(count / 10)
    while m != 0:
        p = p + (m % 10) * count
        count = int(count / 10)
        m = int(m / 10)
    if x == p:
        print("yes")
    else:
        print("no")


palindrome(1001)
