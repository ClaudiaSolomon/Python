# 11
def order_tuple(list_tuple):
    def cheie(tuple_item):
        if len(tuple_item) >= 2 and len(tuple_item[1]) >= 3:
            return tuple_item[1][2]
        else:
            return ''
    return sorted(list_tuple, key=cheie)


print(order_tuple([('abc', 'bcd'), ('abc', 'zza')]))
