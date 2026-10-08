s = 'Spanish, Madrid'
ch = 'a'
def where(s, ch):
    l_index = -1
    for index, letter in enumerate(s):
        if letter == ch:
            l_index = index
    return l_index

class Solution:
    def reverse(self, x: int) -> int:
        y = x % 100 % 10
        z = x // 10 % 10
        u = x // 100 % 10
        m = f"{y}{z}{u}"
        return int(m)
#

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_x = int(str(x)[::-1]) * sign

        if reversed_x < -(2**31) or reversed_x > 2**31 - 1:
            return 0

        return reversed_x