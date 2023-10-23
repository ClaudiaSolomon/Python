# 6
def unique(lista):
    lungime = len(lista)
    lungime_unique = len(set(lista))
    return lungime_unique, lungime - lungime_unique


print(unique([1, 2, 2, 2, 3, 4, 5, 5]))
