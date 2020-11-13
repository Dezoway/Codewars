def reverse(words):
    array =[x[::-1] for x in words.split(" ")]
    return ' '.join(array)







print(reverse('double  space  worlds'))