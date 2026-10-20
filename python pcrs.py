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