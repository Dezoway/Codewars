def rot13 (message):
    alphavit="abcdefghijklmnopqrstuvwxyz"
    intab=alphavit[0:13]
    outtab=alphavit[13:26]
    translator=str.maketrans(intab,outtab)
    translator2=str.maketrans(outtab,intab)
    txt=''
    j=[]
    for x in range(len(message)):
        if message[x].isupper():
            j.append(x)
    for x in message:
        if x.lower() in intab:
            txt += x.lower().translate(translator)
        elif x.lower() in outtab:
            txt += x.lower().translate(translator2)
    for x in j:
        txt.index() =txt.upper()
    return txt









print(rot13("Grfg"))
print(rot13("Pbqrjnef"))
print(rot13("vfgjryir"))