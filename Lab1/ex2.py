# 2
def vowels(string):
    count = 0
    for i in range(len(string)):
        if string[i] in "aeiouAEIOU":
            count = count + 1
    print(count)


vowels("ana are mere si pere")
