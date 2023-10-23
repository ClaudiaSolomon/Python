# 5
def main_diag(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i > j:
                a[i][j] = 0
    return a


print(main_diag([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
