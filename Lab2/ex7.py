# 7
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
        return "yes"
    else:
        return "no"


def palindrome_tuple(list_nr):
    count = 0
    maxi = 0
    for x in list_nr:
        if palindrome(x) == "yes":
            count = count + 1
            if x > maxi:
                maxi = x
    tuple_p = (count, maxi)
    return tuple_p


print(palindrome_tuple([121, 234, 1001]))
