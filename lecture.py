# import doctest
# def scholarship(cgpa: float, year_of_study: int, major: str) -> float:
#     """Requirements for being eligible for a scholarship are having CGPA above 3.7 and studying in 2 or 3 year of study
#     >>> scholarship(3.8, 2, 'CS')
#     True
#     >>> scholarship(3.5, 3, 'Computer Science')
#     False """
#     if (major == "CS" or major == "cs" or major == "Computer Science"):
#         if (cgpa > 3.7):
#             if (year_of_study == 2 or year_of_study == 3):
#                 return True
#             else:
#                 return False
#         else:
#             return False
#     else:
#         return False
#
# print(scholarship(3.8, 1, "Biology"))
# print(scholarship(4.0, 2, "Chemistry"))
# doctest.testmod()
#

# import random
# def generate_random_text(length: int) -> str:
#     head=['a', 'b', 'c', 'd']
#     for i in range(length):
#         head.append(random.choice(head))
#     return ''.join(head)
# output = generate_random_text(1296)
# print("\n".join(output[a:a + 100] for a in range(0, len(output), 100)))

def mystery_math(n: int) -> float:
    """
    Return the expansion provided in the lecture.
    """
    res = 0
    for i in range(1, n + 1):
        res += 1 / (i * i)
    return (6 * res) ** 0.5

print(mystery_math(10))

def swap_neighbours(s: str) -> str:
    """
    Swap all neighbouring letters of a given string.
    """
    em = ''
    for i in range(0, len(s) - 1, 2):
        em += s[i + 1] + s[i]

    if len(s) % 2 == 1:
        em += s[-1]
    return em

print(swap_neighbours('abcdefg'))


def divisible_by_7(lst: list[int]) -> bool:
    """Return True if and only if lst contains an element divisible
    by 7. Otherwise, return False.

    >>> divisible_by_7([4,8,21,6])
    True
    >>> divisible_by_7([1,2,8,9])
    False
    """
    for num in lst:
        if num % 7 == 0:
            return True
    return False