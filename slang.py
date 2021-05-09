import re
def young_slang(text):
    words1 = {
        'be': 'b',
        'are': 'r',
        'you': 'u',
        'please': 'plz',
        'people': 'ppl',
        'really': 'rly',
        'have': 'haz',
        'know': 'no',
        'to': '2',
        'too': '2',
        'TO': '2',
        'TOO': '2',
        'Too': '2',
        'fore': '4',
        'for': '4',
        'oo': '00',
        's': 'z',
        'BE': 'B',
        'Be': 'B',
        'ARE': 'R',
        'YOU': 'U',
        'PLEASE': 'PLZ',
        'PEOPLE': 'PPL',
        'REALLY': 'RLY',
        'HAVE': 'HAZ',
        'KNOW': 'NO',
        'FOR': '4',
        'FORE': '4',
        'OO': '00',
        'Oo': '00',
        'oO': '00',
        'S': 'Z'
    }
    new_text = []
    for i in words1.keys():
        text = re.sub(i, words1[i], text)
    text = re.sub(r',', '', text)
    text = text.replace('.', '')
    text = text.replace("'", '')
    if text[0] == 'w' or text[0] == 'W':
        text = text.split()
        text.insert(0,'LOL')
        text = ' '.join(text)
    '''if len(text) >= 32:
        print(text)
        print(len(text))
        text = text.split()
        if text[0] == 'LOL':
            text.insert(1, 'OMG')
        else: text.insert(0, 'OMG')
        text = ' '.join(text)'''
    if text[0] == 'h' or text[0] == 'H':
        text = text.upper()
    else:
        text = ' '.join([z.upper() if x % 2 == 0 else z for x, z in enumerate(text.split())])
    if '?' in text:
        count = ''
        for x in text.split():
            if x != ' ':
                count += '?'
        text = text.replace('?', count)
    if '!' in text:
        count = ''
        p = 0
        for x in text.split():
            if x != ' ':
                p += 1
                if p % 2 == 1:
                    count += '!'
                else: count += '1'
        text = text.replace('!', count)
    length = len([x for x in text if x != '!' and x != '1'])
    if length >= 32:
        print(text)
        print(len(text))
        text = text.split()
        if text[0] == 'LOL':
            text.insert(1, 'OMG')
        else:
            text.insert(0, 'OMG')
        text = ' '.join(text)

    return text
print(young_slang("After conversions, this should be!"))