def pangram(string):
    alphavit = str('qwertyuiopasdfghjklzxcvbnm')
    if bool([x for x in alphavit if x not in string.lower()]):
        print([x for x in alphavit if x not in string])
        return False
    return True

print(pangram("The quick, brown fox jumps over the lazy dog!"))
print(pangram("vafla"))
print(pangram('Cwm fjord bank glyphs vext quiz is a pangram'))