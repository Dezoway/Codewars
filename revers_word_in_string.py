from functools import reduce
def spin_words(sentence):
    sentence = sentence.split(" ")
    if len(sentence) == 1:
        return sentence[0][::-1]
    sentence=list(map(lambda x: x[::-1] if len(x) >= 5 else x, sentence))
    return ' '.join(sentence)





print(spin_words("Welcome"))
print(spin_words('This sentence is a sentence'))
print(spin_words('to'))