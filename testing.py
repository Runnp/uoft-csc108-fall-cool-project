s = 'Spanish, Madrid'
ch = 'a'
def where(s, ch):
    l_index = -1
    for index, letter in enumerate(s):
        if letter == ch:
            l_index = index
    return l_index

a = 123
print (a % 100 // 10)