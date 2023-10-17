# 8
def div_ascii(x=1, list_strings, flag=True):
    list_of_list_ch = []
    for string in list_strings:
        list_of_ch = []
        for i in range(len(string)):
            if (ord(string[i]) % x == 0 and flag == True) or (ord(string[i]) % x != 0 and flag == False):
                list_of_ch.append(string[i])
        list_of_list_ch.append(list_of_ch)
    return list_of_list_ch


print(div_ascii(2, ["test", "hello", "lab002"], False))
