print(int(99.9))
print('hello', '-', 'how', '-', 'are', '-', 'you')
print(len('aabbcc') == 6)
print('abc123'.isdigit())
print('apple'.upper().isupper())
print('abc123'.isalnum())
print('12.34'.isalnum())

s = 'pineapple'

print(s[4:9])

print(s[-5:])

print(s[-5:-1])

print(s[5:9])

print(s[4:len(s)])

print(s[5:])

robot = 'R2D2'

print(robot.isupper())
print(robot.isalpha())
print(robot.isalnum())
print(robot.isdigit())

s = 'carrot'
print(s[:3])
print(s[-1:3])
print(s[-6:3])
print(s[0:4])
print(s[-6:-3])
print(s[-6:4])

a = "Hello, World!"
print(len(a))


def swap_ends(message: str) -> str:
    last_char = message[-1]
    first_char = message[0]
    end = len(message) - 1
    print(end)
    middle = message[1:4]
    print(middle)
    return last_char + middle + first_char

swap_ends('cable')

print('how are you?'.isspace())

print('   Hi!   '.strip() == 'Hi!    ')

print('hello'.rfind('l') == 3)

print('007B!'.isupper())

name = 'Bob'

print(f"Hello {name}")
print("Hello {name}")
print(f"Hello (name)")


def stretch_string(s: str, stretch_factors: list[int]) -> str:
    """Return a string consisting of the characters in s in the same order
    as in s, repeated the number of times indicated by the item at the
    corresponding position of stretch_factors.

    Precondition: len(s) == len(stretch_factors) and the items of
                  stretch_factors are non-negative

    >>> stretch_string('Hello', [2, 0, 3, 1, 1])
    'HHllllo'
    >>> stretch_string('echo', [0, 0, 1, 5])
    'hooooo'
    """
    output = ''

    for i in range(len(s)):
        output += s[i] * stretch_factors[i]

    return output


def extract_first_letter_reversed(s: str) -> str:
    """
    Given a sentence <s>, extract the first letter of every word in the
    sentence. A word in this context is defined as any continuous segment of
    alphabetical characters. Return the first letter of every word in reverse.

    Precondition: <s> will contain at least one word.

    >>> extract_first_letter_reversed('simple')
    's'
    >>> extract_first_letter_reversed('two words')
    'wt'
    >>> extract_first_letter_reversed('Welcome Frank, you are in computer science! :)')
    'sciayFW'
    >>> extract_first_letter_reversed('helloworld! How are you?')
    'yaHh'
    """
    selection = ''


    start = True

    for char in s:
        if char.isalpha():
            if start:
                selection = char + selection
                start = False
        else:
            start = True
    return selection
#
# What will the contents of cat.txt look like after the following code is executed?

catlines = ["We looked!", "And we saw him!", "The Cat in the Hat!"]
cat_file = open("cat.txt", "w")
for line in catlines:
    cat_file.write(line)
cat_file.close()

# We looked!And we saw him!The Cat in the Hat!

f = open('budgie_budget.csv')

# Consider this code fragment:
f.readline()
for line in f:
    print(line)
# Which description best matches this code fragment?
# prints every line except the first

# Consider this code fragment:
for line in f:
    print(line)
    f.readline()
# Which description best matches this code fragment?
# prints every second line


# Consider this code:
budget_file = open('budgie_budget.txt', 'w')
budget_file.write('Seed: $10/month')
budget_file.write('Cage: $50')
budget_file.close()
# What will the contents of budgie budget.txt look like after this code is run?
# Seed: $10/monthCage: $50


from typing import TextIO
def is_correct(dictionary: TextIO, word: str) -> bool:
    """Return True iff word is a correctly-spelled word in dictionary.

    Note: due to a PCRS-specific constraint, the example calls below use Open
    with a capital 'O'.  The actual function has a lowercase 'o'.

    >>> dict1 = Open('dict.txt', 'r')
    >>> is_correct(dict1, "Zyrtec")
    True
    >>> dict1.close()

    >>> dict1 = Open('dict.txt', 'r')
    >>> is_correct(dict1, "lolz")
    False
    >>> dict1.close()
    """
    for line in dictionary:
        if line.strip() == word:
            return True
    return False


"""
Select all valid methods that can be called on an open file object in Python.
file.read(size)
file.writable()
file.close()
file.truncate()
"""


# Consider this code:
# def num_same(s1: str, s2: str) -> list[int]:
#     """Return a two-item list with the first item representing the number of characters
#     that are the same at corresponding positions of s1 and s2, and the second item
#     representing the number of characters that are different at those positions.
#     >>> num_same('hello', 'jello')
#     [4, 1]
#     >>> num_same('him', 'this')
#     [0, 3]
#     """
#     same_count = 0
#     different_count = 0
#     for i in range(len(s1)):
#         if s1[i] == s2[i]:
#             same_count = same_count + 1
#         else:
#             different_count = different_count + 1
#     return [same_count, different_count]
#
# In which situation will the code above result in an error?
# When s1 is longer than s2.
#
# class Solution:
#     def sortableIntegers(self, nums: List[int]) -> int:
#         n = len(nums)
#
#         fac = []
#         for x in range(1, isqrt(n) + 1):
#             if n % x == 0:
#                 fac.append(x)
#                 if n // x != x:
#                     fac.append(n // x)
#
#         target = sorted(nums)
#
#         def check(nums1, nums2):
#             # Check whether cyclic rotations of nums1 can produce nums2
#             L = len(nums1)
#
#             for i in range(L - 1):
#                 if nums1[i] > nums1[i + 1]:
#                     return nums1[i + 1 :] + nums1[: i + 1] == nums2
#
#             return nums1 == nums2
#
#         ans = 0
#
#         for d in fac:
#             for left in range(0, n, d):
#                 right = left + d - 1
#
#                 if not check(nums[left : right + 1], target[left : right + 1]):
#                     break
#             else:
#                 ans += d
#
#         return ans


# x = 0
# outer = 0
# inner = 0
# while outer < 3:
#     outer = outer + 1
#     while inner < 2:
#         inner = inner + 1
#         x = x + 1
#     x = x + 1
#
#
# answer = 5

['And', 'the', 'fan,', 'and', 'the', 'cup,', 'And', 'the', 'ship,', 'and', 'the', 'fish.']
context_to_next_words = {
    ('And', 'the'): ['fan,', 'ship,'],
    ('the', 'fan,'): ['and'],
    ('fan,', 'and'): ['the'],
    ('and', 'the'): ['cup,', 'fish.'],
    ('the', 'cup,'): ['And'],
    ('cup,', 'And'): ['the'],
    ('the', 'ship,'): ['and'],
    ('ship,', 'and'): ['the']
}

def is_one_to_one(d: dict[str, int]) -> bool:
    """Return True if and only if no two of d's keys map to the same value.

    >>> is_one_to_one({'a': 1, 'b': 2, 'c': 3})
    True
    >>> is_one_to_one({'a': 1, 'b': 2, 'c': 1})
    False
    >>> is_one_to_one({})
    True
    """

    seen = []  # The values that have been seen so far.
    for k in d:
        if d[k] in seen:
            return False
        else:
            seen.append(d[k])

    return True

# Use a list accumulator to keep track of the values we've seen so far.
# For each key in d, if the value associated with that key has already been seen, return False. Otherwise, append it to the list of values that we've seen so far.
# Once all the keys have been processed, return True because we didn't see a duplicate value.


words = ["bat","tab","cat"]
def palindrome_pairs(words: list[str]) -> list[tuple[int, int]]:

    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j:
                combined = words[i] + words[j]

                if combined == combined[::-1]:
                    result.append((i, j))

    return result

#     Return all pairs of indices (i, j) from words where concatenating
#     words[i] and words[j] (in that order) produces a palindrome.
#
#     For example, "bat" and "tab" form a palindrome pair because
#     "battab" is a palindrome. The pair (i, j) means words[i] + words[j]
#     is the palindrome. The order matters, so (i, j) and (j, i) are usually
#     two different results.
#
#     Preconditions: len(words) >= 2
#
#     Example:
#     >>> palindrome_pairs(['abcd', 'dcba'])
#     [(0, 1), (1, 0)]


# Here is the output of help(math.sqrt):
#
# sqrt(...)
#     sqrt(x)
#
#     Return the square root of x.
#
# Assume you have executed this code:
# import math
#
#
# Select the function call that will return the square root of pi.
#
#
#
# sqrt(math.pi)
# math.sqrt(pi)
# math.sqrt(math.pi) - True

# There are two ways to call a method. Below are pairs of method calls; select the pair(s) that are equivalent to each other.
#
#
#
# '\nabc\t\t'.strip()
# str.strip('\nabc\t\t') - True
#
# ['a', 'b', 'c'].count('b')
# list.count('b', ['a', 'b', 'c']) - True
#
# list.append([1, 2, 3], 4)
# [1, 2, 3].append(4)
#
# str.find('Canada is hockey. -Mike Weir', 'a', 2)
# 'Canada is hockey. -Mike Weir'.find('a', 2) - True


# object.method(argument)
# Class.method(object, argument)


# Consider this class definition:
#
# class MyInt(int):
#     """An integer class used for asking in-video quiz questions."""
#
# Some of the following English statements are true and some are false. Select the true one(s).
#
#
# int is a subclass of MyInt.
# MyInt inherits all of the features of int. - True
# An object of type int is an object of type MyInt, but with more features.
# Every method in class int can be called from an object of type MyInt. - True


# class MyInt(int):
#     """An integer class used for asking in-video quiz questions."""
#
# One of the following headers is not a valid method header for this class. Select it.
#
#
# def is_larger(self, other):
# def is_not_zero(): - True
# def is_not_zero(self):
#


# Consider this class definition:
#
# class MyInt(int):
#     """An integer class used for asking in-video quiz questions."""
#
#     def is_between(self, i, j):
#         """Return True iff i <= self <= j
#         """
#
# The type contract is missing above. Below are possible type contracts. Select the one(s) that are not valid for method is_between.
#
#
# (int, MyInt, MyInt) -> bool - True
# (MyInt, int, int) -> bool
# (MyInt, MyInt, MyInt) -> bool
# (int, int, int) -> bool - True

# Consider this doctest code from function remove in vowels.py:
#
#     >>> remove('Harlem Shake')
#     'Hrlm Shk'
#
#
# Select the method(s) that are the unittest equivalent of the doctest above.
#
#
#
# def test_remove(self):
#     act = vowels.remove('Harlem Shake')
#     exp = 'Hrlm Shk'
#     self.assertEqual(act, exp) - True
#
# def test_remove(self):
#     self.assertEqual(vowels.remove('Harlem Shake'), 'Hrlm Shk') - True

# For count_lowercase_vowels_v2, the test cases pass for all chosen values of s ("", "a", "b", "pfffft", "bandit", "aeioua"), except one. When s refers to "aeioua", the actual value is 5, not 6 as expected. Select the possible explanation(s) for this failure.
#
#
# Consonants are being counted.
# No e's are being counted. - True
# Each vowel is only counted once, regardless of the number of occurrences of it. - True
# The first a is not being counted.


# class TestCollectUnderperformers(unittest.TestCase):
#
#     def test_low_threshold(self) -> None:
#         """Test collect_underperformers with a threshold for which there
#         are no underperformers."""
#
#
#         actual = underperformers.collect_underperformers([4, 5, 6], 1)
#         expected = []
#         self.assertEqual(actual, expected)
#
#
#     def test_high_threshold(self) -> None:
#         """Test collect_underperformers with a threshold for which all items
#         are underperformers."""
# 		actual = underperformers.collect_underperformers([4, 5, 6], 8)
#         expected = [4, 5, 6]
#         self.assertEqual(actual, expected)
#
#     def test_mutation(self) -> None:
#         """Confirm that collect_underperformers does not mutate the list
#         it is given."""
# 		actual = [4, 5, 8]
#         underperformers.collect_underperformers(actual, 7)
#         expected = [4, 5, 8]
#         self.assertEqual(actual, expected)


class TestMostPopular(unittest.TestCase):

    def test_one_item(self) -> None:
        """Test most_popular with a dictionary of length 1."""
        company_to_placements = {'Super Shoes': [1, 2, 3]}
        actual = running.most_popular(company_to_placements)
        expected = ['Super Shoes']
        self.assertEqual(actual, expected)

    def test_mutation(self) -> None:
        """Confirm that most_popular does not mutate the dict it is given.
        """
        actual = {'Super Shoes': [1, 2, 3],
                  'Winter Boots': [2, 4],
                  'Speedy Sneakers': [3, 2, 1]}

    running.most_popular(actual)
    expected = {'Super Shoes': [1, 2, 3],
                'Winter Boots': [2, 4],
                'Speedy Sneakers': [3, 2, 1, ]}

    self.assertEqual(actual, expected)

# Consider this code:
#
# def f(L: list[int]) -> int:
#
#     total = 0
#
#     for item in L:
#         for i in range(10):
#             total = total + item * i # The step being considered.
#
#     return total
#
# How does the number of steps grow relative to len(L)?
#
#
#
# The number of steps is constant.
# The number of steps grows logarithmically with respect to len(L).
# The number of steps grows linearly with respect to len(L).
# The number of steps grows quadratically with respect to len(L).

# Which of the following calls return(s) -1?
#
#
#
# linear_search([1, 2, 3], 1)
#
# linear_search([4, 2, -8], 8)
#
# linear_search(['a', 'a', 'a'], 'a')
#
# linear_search([], 0)


# Given a list of 100,000 items, the binary search algorithm eliminates 50,000 items with one comparison. How many items would linear search have to examine to reach the same point?
#
#
# 1
# 50,000 - True
# 100,000
# 50

# What information allows the binary search algorithm to be so much faster than linear search?
#
#
# Binary search uses smaller lists.
# Binary search uses a while loop with only one condition; linear search requires two subexpressions in the condition.
# Binary search requires the list to be sorted.

# If we count the loop condition as 1 step, each comparison as 1 step, each call on function print as 1 step, and each assignment statement as 1 step, in 1 iteration how many steps are there in the worst case?
#
# while i < len(L):
#     if i % 2 == 0:
#         print(i, 'is even')
#     elif i % 3 == 0:
#         print(i, 'is not even and is divisible by 3')
#     elif i % 5 == 0:
#         print(i, 'is not even nor divisible by 3, but is divisible by 5')
#     i = i + 1
#
#
# 1
# 3
# 5
# 6 - True