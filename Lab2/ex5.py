# 5
def main_diag(a):
    for i in range(len(a)-1):
        a[i+1][i] = 0
    return a


print(main_diag([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
