# 5
def validate_dict(tuple_set, dictionar):
    if len(tuple_set) < len(dictionar):
        return False
    else:
        for t in tuple_set:
            key = t[0]
            if key not in dictionar:
                return False
            value = dictionar[key]
            if value.find(t[2], 1, len(value) - 1) == -1:
                return False
            if value.find(t[1], 0, len(value)) != 0:
                return False
            if not value.endswith(t[3]):
                return False
    return True


print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
                    {"key1": "come inside, it's too cold out", "key3": "this is not valid"}))
print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
                    {"key1": "come inside, it's too cold out", "key2": "start middle winter"}))
