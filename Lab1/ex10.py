# 10
def words(s):
    count = 1
    for i in range(len(s)):
        if s[i] == " " and s[i - 1] != " ":
            count = count + 1
            while s[i] == " ":
                i = i + 1
    print(count)


words("I   have Python  exam")
