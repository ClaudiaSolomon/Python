# 7
def numbers(s):
    nr = 0
    for i in range(len(s)):
        if s[i] in "0123456789":
            while s[i] in "0123456789":
                nr = nr * 10 + int(s[i])
                i = i + 1
            break
    print(nr)


numbers("An apple is 123 USD 123")
