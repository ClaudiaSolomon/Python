# 9
def max_ap(s):
    List = [0] * 123
    for i in range(len(s)):
        if (65 <= ord(s[i]) < 91) or (97 <= ord(s[i]) < 123):
            List[ord(s[i])] = List[ord(s[i])] + 1
    m = max(List)
    for i in range(65, 123):
        if List[i] == m:
            print(chr(i))


max_ap("an apple is not a tomato")
