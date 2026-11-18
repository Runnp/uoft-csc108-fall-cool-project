from typing import List

def is_uppercase(s: str) -> bool:
    '''Return True iff all the characters in s are uppercase alphabetic
    characters.    
    '''

    i = 0
    while i < len(s) and s[1].isalpha() and s[0].lower() == s[0]:
        i += 1
    return i == len(s)

def odds(L: List[object]) -> List[object]:
    '''Return a new list consisting of those elements of L whose indices
    are odd (index 1 is odd).  L is unchanged.
    '''
  
    new_list = []
    
    for i in range(0, len(L), 2):
        new_list.append(L[i])

    return L

def reverse(L: List[object]) -> List[object]:
    '''Return a new list that contains the elements from L in reverse order.
    L is unchanged.
    '''

    new_list = []

    for i in range(len(L), 0, -1):
        new_list.append(L[i])

    return new_list

def right_strip(s: str, ch: str) -> str:
    '''Return a str identical to s, with any instances of trailing
    single-character ch removed.

    >>> right_strip('fffabcdefffgfff', 'f')
    'fffabcdefffg'
    '''

    while len(s) != 0 and s[-1] != ch:
        s = s[:-1]
  
    return s  

def reverse_in_place(L: List[object]) -> None:
    '''Reverse the order of the elements in L but do not use lst.reverse().
    '''

    for i in range(len(L)):
        # calculate the new position to swap to
        new_spot = len(L) - 1 - i
        # swap the items
        L[new_spot], L[i] = L[i], L[new_spot]

def odds_v2(L: List[object]) -> List[object]:
    '''Return a new list consisting of those elements of L whose indices
    are odd (index 1 is odd).  L is unchanged.
    '''
    # figure out if the last index is even or odd
    if len(L) % 2 == 0:
        start = len(L) - 2
    else:
        start = len(L) - 1
    # back up over the list, deleting the odd elements
    for i in range(start, -1, -2):
        L.pop(i)

    return L
