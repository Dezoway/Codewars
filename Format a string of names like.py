def namelist(names):
    k=""
    if len(names) == 1:
        return (names[0]["name"],"Wrong output for a single name")
    elif len(names) <1:
        return "Must work with names"
    for x in names:
        if len(names[:names.index(x)]) == len(names)-2:
            k+="{} {} ".format(x.get("name"),"&")
            continue
        k += "{}, ".format(x.get("name"))
    return k[:-2]

print(namelist([{"name": "Bart"}, {"name": "Lisa"}, {"name": "Maggie"}, {"name": "Gomer"}, {"name": "Marge"}]))
print(namelist([{"name": "Bart"}, {"name": "Lisa"}, {"name": "Maggie"}]))
print(namelist([{"name": "Bart"}, {"name": "Lisa"}]))
print(namelist(([{"name":"Bart"}])))