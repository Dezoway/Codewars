def rank(st,we,n):
    if n > len(we):
        return "Not enough participants"
    elif len(st) == 0:
        return "No participants"
    else:

        Alphavite="abcdefghijklmnopqrstuvwxyz"                      #these are sketches
        st1=st.split(",")
        som=0
        som1=[]
        som2=[]
        for x in st1:
            for z in x.lower():
                som+=Alphavite.index(z)+1
            som1.append((som+len(x))*we[st1.index(x)])
            som2.append((som+len(x))*we[st1.index(x)])
            som1.append(x)
            som=0
        som2.sort(reverse=True)
        num=som2[n-1]
        return(som1[som1.index(num)+1])


print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4))
print(rank("Lagon,Lily", [1, 5], 2))
print(rank("", [4, 2, 1, 4, 3, 1, 2], 4))