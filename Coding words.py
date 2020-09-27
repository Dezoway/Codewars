vowel='aeuio'
digits='12345'

def identification(words):
    j=0
    for x in words:
        if x.isdigit():
            j=+1
    if j==0:
        print(coding(words))
    else:
        print(decoding(words))



def decoding(words):
    maketr=str.maketrans(digits,vowel)
    return words.t





def coding(words):
    maketr=str.maketrans(vowel,digits)
    return words.translate(maketr)


identification("hello")
identification('h2ll5')

