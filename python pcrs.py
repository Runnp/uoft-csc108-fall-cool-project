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