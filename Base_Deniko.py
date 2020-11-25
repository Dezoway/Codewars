def de_nico(key, string):
    key1 = sorted(key)
    dictionary_list = {i: x for x, i in enumerate(key1)}
    list_index = list()
    new_list_string = list()
    count = 0
    for x in key:
        if x in dictionary_list:
            list_index.append(dictionary_list[x])
    while True:
            if count == len(string):
                break
            new_string = string[count:]
            for x in list_index:
                try:
                    new_list_string.append(new_string[x])
                    count += 1
                except IndexError:
                    continue

    return ''.join(new_list_string).rstrip()





print(de_nico('crazy','cseerntiofarmit on'))
print(de_nico('crazy', 'cseerntiofarmit on  '))
print(de_nico('ba', '2143658709'))
print(de_nico('mdve','duvlqrmimhpzb mfrxwiezmxnyzgakbowoelnab'))