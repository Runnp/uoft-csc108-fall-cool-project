# def michael_function(points):
#     result = 0
#     for i, value in enumerate(points):
#         if i % 2 == 0:
#             result += value
#     return result
#
# print(michael_function([3, 10, 11, 12, 9]))

# def second_largest(numbers):
#     largest = second = numbers[0]
#     for num in numbers[1:]:
#         if num > largest:
#             second = largest
#             largest = num
#         elif num > second:
#             second = num
#     return second
#
# print(second_largest([1,2,3,4,5,6,7,8,9]))

# with open("practical.txt") as source:
#     values = source.readline().strip().split(";")
#     print(values)


# file = open("practical.txt")
# A = file.readline()
# # print(A)
# B = file.readline()
# # print(B)
# C = file.readline()
# # print(C)
# D = file.readline()
# print(D)

# file = open("practical.txt")
# for line in file:
#     if int(line) >= 30:
#         print(line, end="")

# file = open("companies.txt")
#
# for line in file:
#     data = line.split("|")
#
#     if data[2] == "125":
#         print(data[0])

# file = open("practical.txt")
# for line in file:
#     data = line.split("|")
#
#     if len(data) >= 3 and data[2].strip() == "125":
#         print(data[0])
#         # Since the first line has three elements, but its last value is "125\n" and not "125", the comparison fails.
        # In this case, .strip() fixes the issue, while len(data) >= 3 prevents the cases where lines might have less
        # than three elements

# with open(input_filename, "r") as input_file:
#     with open(output_filename, "w") as output_file:
#         for line in input_file:
#             data = line.strip().split("|")
#             revenue = int(data[2])
#             if revenue >= minimum:
#                 output_file.write(data[0] + "," + data[2] + "\n")

# x = 0
# outer = 0
# inner = 0
# while outer < 3:
#     outer = outer + 1
#     while inner < 2:
#         inner = inner + 1
#         x = x + 1
#     x = x + 1
# print(x)

name_to_binomial = {'human': 'Homo sapiens',
                    'dog': 'Canis familiaris',
                    'narwhal': 'Monodon monoceros'}

print('dog' in name_to_binomial)
# print('Canis familiaris' in name_to_binomial)
# print(name_to_binomial[0] == 'human')
print(len(name_to_binomial) == 3)
print(name_to_binomial == {'dog': 'Canis familiaris', 'narwhal': 'Monodon monoceros', 'human': 'Homo sapiens'})


def build_placements(shoes: list[str]) -> dict[str, list[int]]:
    """Return a dictionary where each key is a shoe company from shoes and each
    value is a list of placements by people wearing footwear made by that
    company. First place is at index 0 of shoes, 2nd place is at index 1, and
    so on.

    >>> build_placements(['Saucony', 'Asics', 'Asics', 'NB', 'Saucony', \
                          'Nike', 'Asics', 'Adidas', 'Saucony', 'Asics'])
    {'Saucony': [1, 5, 9] 'Asics': [2, 3, 7, 10], 'NB': [4], 'Nike': [6], 'Adidas': [8]}
    """

    rank = {}
    track = 1

    for brand in shoes:
        if brand not in rank:
            rank[brand] = []
        rank[brand].append(track)
        track += 1

    return rank


def isAnagram(s1: str, s2: str) -> bool:
    """Return True if s2 is an anagram of s1, False otherwise.
    Two strings are anagrams of each other if they contain the same
    count of all characters. Case sensitive and space sensitive.
    """
    return sorted(s1) == sorted(s2)


def tuple_max(l: list[tuple[int, int]]) -> int:
    """Return the index of the largest tuple in l.
    The max is determined by the 2nd int in each tuple.
    Return -1 if l is empty.
    If multiple tuples have the same 2nd int, return the first.

    >>> tuple_max([(1, 0), (2, 0), (-4, 1)])
    2
    """
    if len(l) == 0:
        return -1


    max_index = 0
    for i in range(len(l)):
        if l[i][1] > l[max_index][1]:
            max_index = i

    return max_index

# 9: 'steak',
# 9: 'cake'
# Python dictionaries cannot contain duplicate keys. The later value replaces the earlier one.

# Dictionaries do not support .append()!
# .append() is a method for lists.

def reverse_lookup_dictionary(phone_num: str,
                              phone_to_name: dict[str, str]) -> str:
    """This function receives a phone number phone_num, and a dictionary
    phone_to_name in which each key is a phone number and each value
    is the name associated with that phone number.

    Return the name associated with phone_num in phone_to_name, or
    an empty string if there is no match.

    >>> reverse_lookup_dictionary("416-555-3498", {"416-555-3498": \
        "John A. Macdonald", "647-555-9812": "Louis Riel", "416-555-6543": \
        "Canoe Head", "905-555-6681":"Tim Horton"})
    'John A. Macdonald'
    """
    if phone_num in phone_to_name:
        return phone_to_name[phone_num]

    return ''