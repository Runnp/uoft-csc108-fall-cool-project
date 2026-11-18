from typing import List


def is_uppercase(s: str) -> bool:
    '''Return True iff all characters in s are uppercase alphabetic characters.'''
    i = 0
    while i < len(s) and s[i].isalpha() and s[i].upper() == s[i]:
        i += 1
    return i == len(s)


def odds(L: List[object]) -> List[object]:
    '''Return elements at odd indices in a new list. Do not change L.'''
    new_list = []
    for i in range(1, len(L), 2):
        new_list.append(L[i])
    return new_list


def reverse(L: List[object]) -> List[object]:
    '''Return a new reversed list, leaving L unchanged.'''
    new_list = []
    for i in range(len(L) - 1, -1, -1):
        new_list.append(L[i])
    return new_list


def right_strip(s: str, ch: str) -> str:
    '''Remove trailing copies of ch, without using str methods.'''
    while len(s) != 0 and s[-1] == ch:
        s = s[:-1]
    return s


def reverse_in_place(L: List[object]) -> None:
    '''Reverse the given list itself without list.reverse().'''
    for i in range(len(L) // 2):
        new_spot = len(L) - 1 - i
        L[new_spot], L[i] = L[i], L[new_spot]


def odds_v2(L: List[object]) -> List[object]:
    '''Intentionally buggy original version: demonstrates mutation during testing.'''
    if len(L) % 2 == 0:
        start = len(L) - 2
    else:
        start = len(L) - 1
    for i in range(start, -1, -2):
        L.pop(i)
    return L