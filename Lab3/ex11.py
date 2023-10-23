# 11
def compare(*args, **dictionar):
    lista = []
    count = 0
    for arg in args:
        lista.append(arg)
    for pereche in dictionar.items():
        value = pereche[1]
        if value in lista:
            count += 1
    return count


print(compare(1, 2, 3, 4, x=1, y=2, z=3, w=5))
