s = 'Spanish, Madrid'
ch = 'a'
def where(s, ch):
    l_index = -1
    for index, letter in enumerate(s):
        if letter == ch:
            l_index = index
    return l_index

def reverse(x: int) -> int:
    y = x % 100 % 10
    z = x // 10 % 10
    u = x // 100 % 10
    m = f"{y}{z}{u}"
    return m
print(reverse(123))