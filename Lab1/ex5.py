# 5
def matrix_spiral(n, m, a):
    aux1 = 0
    aux2 = 0
    while aux1 < n and aux2 < m:
        for i in range(aux1, m-aux2):
            print(a[aux1][i])
        for i in range(aux1 + 1, n-aux1):
            print(a[i][m - aux2-1])
        for i in range(m - aux2-2, aux2, -1):
            print(a[n - aux1-1][i])
        for i in range(n - aux1 - 1, aux1 , -1):
            print(a[i][aux2])
        aux1 = aux1 + 1
        aux2 = aux2 + 1


matrix = [['f', 'i', 'r', 's'],
          ['n', '_', 'l', 't'],
          ['o', 'b', 'a', '_'],
          ['h', 't', 'y', 'p']]

matrix_spiral(4, 4, matrix)
