# 12
def rhyme(list_words):
    list_tuple_words = []
    vector_ap = [0] * len(list_words)
    for i in range(len(list_words)):
        tuple_rime = ()
        if vector_ap[i] == 0:
            tuple_rime += (list_words[i],)
            vector_ap[i] = 1
            for j in range(i + 1, len(list_words)):
                if (list_words[i][len(list_words[i]) - 2] == list_words[j][len(list_words[j]) - 2]
                        and list_words[i][len(list_words[i]) - 1] == list_words[j][len(list_words[j]) - 1]):
                    if vector_ap[j] == 0:
                        tuple_rime += (list_words[j],)
                        vector_ap[j] = 1
        if tuple_rime != ():
            list_tuple_words.append(tuple_rime)
    return list_tuple_words


print(rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
