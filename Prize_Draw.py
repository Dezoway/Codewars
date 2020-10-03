from functools import cmp_to_key
def rank(st, we, n):
    if(not st): return "No participants"
    st = st.split(',')
    if(n > len(st)): return  "Not enough participants"
    pairs = [(name,word(name.lower())*we[i]) for i, name in enumerate(st)]
    pairs = sorted(pairs,key=cmp_to_key(compare))
    return pairs[n-1][0]
def word(x): return len(x)+sum(ord(chr) - ord('a') + 1 for chr in x)
def compare(x,y):
    if x[1] == y[1]:
        if x[0] == y[0]: return 0
        if x[0] > y[0]: return 1
        return -1
    return y[1] - x[1]








print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4))
print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [7, 2, 2, 6, 3, 1, 2], 4))
print(rank("Lagon,Lily", [1, 5], 2))
print(rank("", [4, 2, 1, 4, 3, 1, 2], 4))