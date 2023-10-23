# 10
def loop(dictionar):
    lista = []
    x = dictionar["start"]
    del dictionar["start"]
    for pereche in dictionar.items():
        if x == pereche[0] and pereche[1] not in lista:
            lista.append(x)
            x = pereche[1]
        if pereche[1] in lista:
            break
    return lista


mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
print(loop(mapping))
