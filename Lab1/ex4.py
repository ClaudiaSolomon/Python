# 4
def c_to_s(s1):
    s2 = ""
    for i in range(len(s1)):
        if s1[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if i == 0:
                s2 = s2 + s1[i]
            else:
                s2 = s2 + "_" + s1[i]
        else:
            s2 = s2 + s1[i]
    print(s2.lower())


c_to_s("AnaAreMere")
