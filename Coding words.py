WORDING = {"a": 1, "e": 2, "i": 3, "u": 4, "o": 5}  # To make a letter represent a specific character we use a tuple


def coding(words):
    for x in WORDING.keys():  # Using this loop, we iterate through the keys in the tuple in the form of letters
        if x in words:  # Next,if this key, that is, the letter is in our string
            words = words.replace(x, str(WORDING[x]))   # We equate our word characters by replacing the key:value
    return words


def encoding(words):
    pass


print(coding('hello'))
