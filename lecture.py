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
#
# def mystery_math(n: int) -> float:
#     """
#     Return the expansion provided in the lecture.
#     """
#     res = 0
#     for i in range(1, n + 1):
#         res += 1 / (i * i)
#     return (6 * res) ** 0.5
#
# print(mystery_math(10))
#
# def swap_neighbours(s: str) -> str:
#     """
#     Swap all neighbouring letters of a given string.
#     """
#     em = ''
#     for i in range(0, len(s) - 1, 2):
#         em += s[i + 1] + s[i]
#
#     if len(s) % 2 == 1:
#         em += s[-1]
#     return em
#
# print(swap_neighbours('abcdefg'))
#
#
# def divisible_by_7(lst: list[int]) -> bool:
#     """Return True if and only if lst contains an element divisible
#     by 7. Otherwise, return False.
#
#     >>> divisible_by_7([4,8,21,6])
#     True
#     >>> divisible_by_7([1,2,8,9])
#     False
#     """
#     for num in lst:
#         if num % 7 == 0:
#             return True
#     return False

# s = ''
# def echo() -> None:
#     s = input('... ')
#
#     while s != "stop it!":
#         print(s)
#         s = input('... ')
# echo()

# def differentiate(f: int, x: int) -> float:
#     # f needs to recognize x
#     p = 0
#     h = 1
#     while h != 0:
#         h /= 0.1
#         p = ((f + h) - f) / h
#
#     f = (6 - (x + h)) ** 1/2
#     h = 1
#     while h != 0:
#         h /= 0.1
#         p = ((f + h) - f)/h
#         print(p)
#
# def find_derivative_v2() -> None:
#     tolerance = 10 ** (-4)
#     i = 0
#     h = 10 ** (-1*i)
#     x = 2
#     prev_value = 0
#     f_prime = ((6 - (x+ h)) ** (0.5) - (6 - x) ** (0.5)) / h
#     print("f'(" + str(x) + ") =" + str(f_prime) + "for h =" + str(h))
#     while abs(f_prime - prev_value) > tolerance:
#         i += 1
#         h = 10 ** (-1 * i)
#         f_prime = ((6 - (x + h)) ** (0.5) - (6 - x) ** (0.5)) / h
#         prev_value = f_prime
#     return f_prime


# def count_a(file: str) -> int:
#     with open(file, "r") as f:
#         lines = f.read()
#         count = lines.count("a")
#     return count
#
# print(count_a(file))


#
# file = "/Users/runnp/PycharmProjects/uoft-csc108-fall-cool-project/stixi.txt"
# def num_empty_lines(file: str) -> int:
#     """
#     Return total number of empty lines in the file.
#     """
#     c = 0
#     with open(file, "r") as f:
#         for line in f:
#             if line == "\n":
#                 c = c + 1
#     return c
#
# print(num_empty_lines(file))
#
#
# song = "/Users/runnp/PycharmProjects/uoft-csc108-fall-cool-project/song.txt"
# def obtain_song(song: str) -> list[str]:
#     """
#     Return a list of words from the song file.
#     :param song:
#     :return:
#     """
#     with open(song, "r") as f:
#         lines = f.readlines()
#         words = []
#         for line in lines:
#             words.append(line.strip())
#     return words
# print(obtain_song(song))
#
# csv = "/Users/runnp/PycharmProjects/uoft-csc108-fall-cool-project/musicians.csv"
# def highest_rated_musician(csv: str) -> str:
#     """
#     Return the highest rated musician from the csv file.
#     :param csv:
#     :return:
#     """
#     with open(csv, "r") as f:
#         f.readlines()
#         high_rated_musicians = 0
#         answer = ''
#         musicians = []
#         for line in f:
#             line = line.strip(",")
#             musicians_name = line[0]
#             musicians_rating = int(line[1])
#
#             if musicians_rating > high_rated_musicians:
#                 answer = musicians_name
#                 high_rated_musicians = musicians_rating
#
#     return answer
# print(highest_rated_musician(csv))
#
# def freq(in_filename:str, out_filename:str) -> None:
#     """
#     Write the count of each digit found in in_filename to out_filename
#
#     Precondition: each line contains exactly one digit
#     :param in_filename:
#     :param out_filename:
#     :return:
#     """
#     with open(in_filename,'r') as infile:
#         counts = [0] * 10
#         for line in infile:
#             digit = int(line)
#             counts[digit] += 1
#
#     with open(out_filename,'w') as outifle:
#         for digit in range(10):
#             outifle.write(str(counts[digit]))
#
# if __name__ == '__main__':
#     in_filename = 'digits.txt'
#     out_filename = 'frequency.txt'
#
#
# def split_names(filename: str) -> None:
#     """
#     Write first names into first.txt
#     Write last names into last.txt
#     Precondition: each line contains at least one first and one last name
#
#     :param filename:
#     :return:
#     """
#     with open(filename, 'r') as source:
#         with open('first.txt', 'w') as first:
#             with open('second.txt', 'w') as second:
#                 for line in source:
#                     names = line.split()
#
#                     first.write(names[0] + '\n')
#                     second.write(names[1] + '\n')
#
# def check_free_shipping(order_total: float, membership_status: str, location: str) -> str:
#     if order_total > 50 and membership_status == 'premium' and location == 'domestic':
#         return 'Free shipping'
#     return 'No free shipping'
#
# def foo(x, y):
#     if x > 100 and y > 0:
#         if y > 100 or x > 100:
#             return "A"
#         return "B"
#     elif y <= 0 or x <= 0:
#         return "A"
#     else:
#         if y > 0:
#             return "A"
#         if y <= 0:
#             return "B"
#         else:
#             return "D"
#
# def char_index(s: str) -> dict[str, list[int]]:
#     dictionary = {}
#
#     for i, char in enumerate(s):
#         if char not in dictionary:
#             dictionary[char] = []
#
#         dictionary[char].append(i)
#
#     return dictionary
#
# print(char_index("nnMMRRiiZZhhAAAvvOO"))

# Which of these can be a key? (for dictionaries)
# a) string - True
# b) int - True
# c) list
# d) tuple - True
# need to be immutable
# a = {1: 'a', 1: 'a', 1: 'a'}
# will not return an Error
# a returns {1: 'a'}
# Since int are immutable, Python recognizes that all these are the same and return that
# t = (5)
# type(t) is <class 'int'>
# t = (5,)
# type(t) is <class 'tuple'>

book_series = {'Animorphs': {'author': 'K.A. Applegate', 'number': 54, 'genre':
'middle grade'},
'Inheritance Games': {'author': 'Jennifer Lynn Barnes', 'number': 2,
'genre': 'adult'},
'Shopaholic': {'author': 'Sophie Kinsella', 'number': 10, 'genre':
'adult'}}

def find_books(book_series: dict[str, dict], genre: str) -> list[str]:
    series_list = []
    for series in book_series:
        if book_series[series]['genre'] == genre:
            series_list.append(series)
    return series_list

# * 6/11/26
# * Lecture
# * Thursday November 12
# * File IO
# * 20 Pages, Questions 14 Pages
# * LearnAid
# * MockTest
# *
# * 6/11/26
# * Lecture
# * Thursday November 12
# * File IO
# * 20 Pages, Questions 14 Pages
# * LearnAid
# * MockTest
# * Poll:
# * B
# * C
# * D
# * B
# * B
# * D

def in_trie(word: str, trie: dict[str, dict]) -> bool:
    curr_dict = trie
    for ch in word:
        if ch not in curr_dict:
            return False
        curr_dict = curr_dict[ch]
    return True

def make_dictionary(filename: str) -> dict[str, list[str]]:
    """
    Return a dictionary where the keys are words in <filename> and the value
    for a key is the list of words that were found to follow the key.
    """
    with open (filename) as f:
        words = f.read().split()

    word_d = {}
    prev_word = ''
    for word in words:
        if prev_word not in word_d:
            word_d[prev_word] = []
        word_d[prev_word].append(word)
        prev_word = word
    return word_d

# print(make_dictionary('alice.txt'))

# *
# * 9/11/26
# * Lecture
# * def trie
# * Random Text Generator
# * capitalization matters
# * punctuation stays attached
# * key: a word
# * value: the list of every word that came after it

# animal_to_locomotion = {'fish' : ['swim'],
#                         'kangaroo' : ['hop'],
#                         'frog' : ['swim', 'hop']}
# animal_to_locomotion['human'] = ['swim', 'run', 'walk', 'airplane']
#
# Will an error occur when the code is executed?
# yes
# no
# no is the right answer


# animal_to_locomotion = {'fish' : ['swim'],
#                         'kangaroo' : ['hop'],
#                         'frog' : ['swim', 'hop']}
# animal_to_locomotion['kangaroo'].append('airplane')
# Will the number of key/value pairs in the dictionary increase?
# yes
# no

# def express_checkout(product_to_quantity: dict[str, int]) -> bool:
#     """Return True iff the grocery order in product_to_quantity qualifies for
#     the express checkout.  product_to_quantity maps products to the numbers of
#     those items in the grocery order.
#
#     >>> express_checkout({'banana': 3, 'soy milk': 1, 'peanut butter': 1})
#         True
#     >>> express_checkout({'banana': 3, 'soy milk': 1, 'twinkie': 5})
#         True
#     """
#     total = 0
#
#     for product in product_to_quantity:
#         total += product_to_quantity[product]
#
#     if total <= 9:
#         return True
#     else:
#         return False

# docstring testing
# testing domain
# divide doc strings into meaningful categories
# size
# boundary - abs
# dichotomy - vowels / non-vowels, even / odds
# order - non-decreasing, non-increasing
# docstrings must include the four categories of testing
# power function
# doctests:
# mystery(1, -2)
# mystery(10, 1000000)
# mystery(-5, 2)
# mystery(0, 3)
# 0 ** 0 = 1 in python console
# ELLIPSIS: helo ...
# if __name__ == '__main__':
#   import doctest
#   doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)
#
#
#

def absolute_value(integer: int) -> int:
    """
    Return the absolute value of an integer.
    >>> absolute_value(-108)
    108
    >>> absolute_value(-10 ** 6)
    1000000

    """
    return abs(integer)

# 16/11/26
# Lecture
# def test_
# input_val = 1
# expected = 0
# self.assertEqual(expected, result)
# MSG.format(input_val, expected, result))
# unittest.main

#
# def remove_shared(L1: list, L2: list) -> None:
#     """Remove items from L1 that are in both L1 and L2.
#     """
#
#     for v in L2:
#         if v in L1:
#             L1.remove(v)
#
#
# Here is a
# unittest
#
#
# class with a single test case for this function.The expected values are not shown.
#
#
# import unittest
#
#
# class TestRemoveShared(unittest.TestCase):
#     """Tests for function duplicates.remove_shared."""
#
#     def test_full_overlap(self):
#         """
#         Test remove_shared where the two lists have the
#         same items, but the order is different.
#         """
#
#         list_1 = [1, 2, 3]
#         list_2 = [3, 2, 1]
#         list_1_expected =  # What is the expected value for list_1?
#         list_2_expected =  # What is the expected value for list_2?
#
#         remove_shared(list_1, list_2)
#
#         self.assertEqual(list_1, list_1_expected)
#         self.assertEqual(list_2, list_2_expected)
#
#
# if __name__ == '__main__':
#     unittest.main(exit=False)
#
# Select
# the
# correct
# code
# fragment
# for this test case:
#
#     list_1_expected = []
#     list_2_expected = [3, 2, 1]

# Consider this code, which is in a file called words.py:
#
# def word_frequency(letter_to_words: dict[str, list[str]]) -> dict[str, int]:
#     """Return a dictionary where the keys are the letters from letter_to_words,
#     and the values are the number of words beginning with that letter in
#     letter_to_words.
#
#     Precondition: the length of each list in letter_to_words is at least 1,
#     each key in letter_to_words is a lowercase letter, and each value is a
#     list of lowercase words beginning with that letter.
#
#     >>> d = {'a': ['apple'], 'b': ['beet', 'banana'], 'c': ['carrot', 'cucumber']}
#     >>> expected = {'a': 1, 'b': 2, 'c': 2}
#     >>> word_frequency(d) == expected
#     True
#     """
#
#
# Consider this unittest method header:
#
# def test_word_frequency(self):
#     """ A dictionary with several items."""
#
#     # Add body here.
#
#
# Select the unittest method body(ies) that are equivalent to the doctest in the word_frequency docstring. You can assume that words has been imported.
#
#
#
#     d = {'a': ['apple'], 'b': ['beet', 'banana'], 'c': ['carrot', 'cucumber']}
#     actual = words.word_frequency(d)
#     expected = {'a': 1, 'b': 2, 'c': 2}
#     self.assertEqual(actual, expected)
#
#     d = {'a': ['apple'], 'b': ['beet', 'banana'], 'c': ['carrot', 'cucumber']}
#     actual = words.word_frequency(d)
#     expected = {'c': 2, 'b': 2, 'a': 1}
#     self.assertEqual(actual, expected)

def test_absolute_value(self):
    """
    Test a positive vlue input
    """
    # test_value, expected = 0, 1
    test_value, expected = -10, 10
    result = absolute_value(test_value)
    self.assertEqual(result, expected)

import unittest

def indices(s: str, substr: str) -> list[int]:
    """
    Return the indices in <s> at which non-overlapping
    copies of <substr> start. <substr> is non-empty.
    """
    i = 0
    found = []
    while i < len(s):
        if s[i: i + len(substr)] == substr:
            found.append(i)
            i += len(substr)
        else:
            i += 1
    return found


MSG = 'Function: {}, input: {}, expected: {}, received: {}.'

class TestIndices(unittest.TestCase):
    """ The unit tests for the indices function. """

    def test_overlap(self):
        """ Tests an input string that contains the substring. """
        # test_str, test_substr = 'Wooowowo', 'wo'
        # expected = [0, 3, 5]
        # test_str, test_substr = 'Qwertyuiop asdfghjkl zxcvbnm', 'fgh'
        # expected = [14]
        test_str, test_substr = 'Ser quyosh, Xur olkam, Bor jahon', 'o'
        expected = [7, 11, 16, 24, 30]
        result = indices(test_str, test_substr)
        self.assertEqual(expected, result,
            MSG.format('indices()', (test_str, test_substr), expected, result))


# 18/11/26
# Lecture
# Regular Expression
# \d for nums
# \w, \s
import re

txt = '''143-614-3330, 556-732-3881, 680-964-1127, 568-769-3556,
    099-887-1597, 081-997-3959, 842-502-6372, 406-648-1681,
    416-475-8283, 259-778-2868, 105-776-7011, 912-576-5192,
    018-087-9554, 975-845-6860, 702-619-1033, 326-382-3556,
    416-294-6744, 957-135-4565, 667-624-1973, 603-418-9850'''

x = re.findall("416-[0-9]{3}-[0-9]{4}", txt)
print(x)

x = re.findall(r"416-\d{3}-\d{4}", txt)
print(x)
# \w is for letters

# pattern
# \d\.\d.
# text
# pi is 3.14, e is 2.72, 3x14 is 42
# pi is 3.14, e is 2.72, 3x14 is 42
# re.findall(r'\d\.\d.', txt) gives ['3.14', '2.72']

# pattern
# \bis\b
# text
# this is what it is
# this is what it is
# re.findall(r'\bis\b', txt) gives ['is', 'is']

# pattern
# gr(a|e)y
# text
# gray grey groy
# gray grey groy
# re.findall(r'gr(a|e)y', txt) gives ['a', 'e']

# pattern
# M[iy]ke
# text
# Mike Miller, Mick Furrier, Myke Mason, Mike Baker
# Mike Miller, Mick Furrier, Myke Mason, Mike Baker
# re.findall(r'M[iy]ke', txt) gives ['Mike', 'Myke', 'Mike']
import re

def find_specific(txt: str) -> list[str]:
    """ Return a list of matches where the string
        begins with one 'a' followed by one or more 'b'
    >>> find_specific("aaabbbabbacb")
    ['abbb', 'abb']
    >>> find_specific("abbbabaaa")
    ['abbb', 'ab']
    """
    return re.findall(r"ab+", txt)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

import re

def run_me(txt: str, my_regex: str) -> list[str]:
    if len(my_regex) <= 6:
        return re.findall(my_regex, txt)
    return ["Fail"]

def task2_helper(txt: str):
    """ Create a regex that is no more than 6 characters long
        that matches when a string, or substring, starts with
        an 'a' followed by 0 or more numerals and ends
        with the following string: 'CS'
    >>> task2_helper("a998289CSC is great aaCS")
    ['a998289CS', 'aCS']
    >>> task2_helper("aCSC108")
    ['aCS']
    >>> task2_helper("")
    []
    """
    your_regex = r"a\d*CS"
    return run_me(txt, your_regex)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
