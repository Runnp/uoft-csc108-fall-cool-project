#print(3000-711)
#print(49/8)
#print(270//3)
#print(270%3)
from secrets import token_hex

#my_age = 17
#my_friends_age = my_age + 14
#difference = my_friends_age - my_age
#print(difference)

#x = 15
#y = -4
#z = 0.0
#print(y / z)

# your goal is to consume 100g of protein in the day
#consumed = 0
#required = 100
#protein_to_go = required - consumed
# for breakfast you had 4 eggs
#consumed = 4 * 12
# oops. That was the protein for a pair of eggs
#consumed = consumed / 2
# let’s update the protein we have left
#protein_to_go = required - consumed
# now by lunch, you have eaten 65g of protein
#consumed = 65
# by the end dinner, you have eaten 30 more
#consumed = consumed + 30
#print(protein_to_go)
#print(consumed)
#print(required)


#distance = 40
#print("Did you know your distance from school is")
#print(distance)
#print("km?")
#speed = 1.25
#commute_time = distance / speed
#print("and your commute takes")
#print(commute_time)
#print("minutes due to traffic?")
# if there was no traffic you can go even faster
#no_traffic_commute_time = distance / (speed + 0.25)
#print("If you had no traffic your commute would take")
#print(no_traffic_commute_time)
#print("minutes.")
# let's pretend you're closer to the school
#distance = distance - 25
#print("Congrats! Your distance to the school is now")
#print(distance)
#no_traffic_commute_time = distance / (speed + 0.25)
# But see that no_traffic_commute_time hasn't changed
#print("And your no traffic commute time is")
#print(no_traffic_commute_time)

#seconds = 95399
#minutes = seconds // 60
#hours = minutes // 60
#days = hours // 24
#print(seconds, minutes, hours, days)

# Practical Week 2
# Task 1
# def leetcodes_answered(num_weeks: int, questions_per_week: int) -> int:
#     '''Return the total number of leetcode questions done over num_weeks
#     where in each week questions_per_week were answered
#     >>> leetcodes_answered(2, 30)
#     60
#     >>> leetcodes_answered(1, 8)
#     8
#     '''
#     return num_weeks * questions_per_week
# # two of us are doing leetcode but at different rates and different amounts of time
# person_a = leetcodes_answered(2, 8)
# person_b_rate = 30
# person_b = leetcodes_answered(1, person_b_rate)
# grand_total = person_a + person_b
# print("With the two of us combined, we will have done", grand_total, "questions")

# Task 2
# def cookies_needed(adults: int, teens: int, children: int) -> int:
#     '''Return the number of cookies needed to
#     feed this number of adults, teens and children.
#     Each adult eats two, each teen six, and each child three.
#     >>> cookies_needed(2, 3, 1)
#     25
#     '''
#     adults_cookies = 2
#     teen_cookies = 6
#     child_cookies = 3
#     return adults_cookies * adults + teen_cookies * teens + child_cookies * children
#
# def is_multiple_of_7(x: int) -> bool:
#     '''Return True iff 7 divides x without a remainder.
#     >>> is_multiple_of_7(15)
#     False
#     >>> is_multiple_of_7(7)
#     True
#     '''
#     return x % 7 == 0
#
# def is_multiple(x: int, y: int) -> bool:
#     '''Return True iff y divides x without a remainder.
#     >>> is_multiple(15, 3)
#     True
#     >>> is_multiple(7, 2)
#     False
#     '''
#     return x % y == 0
#
#
# Task 3
# def feet_to_meter(f: float) -> float:
#     '''Return the number of meters equivalent to f feet.
#         >>> feet_to_meter(10.0)
#         3.047851264858275
#     '''
#     return f / 3.281
#
# def meter_to_feet(m: float) -> float:
#     '''Return the number of feet equivalent to m meters.
#         >>> meter_to_feet(3.048)
#         10.000488
#         '''
#     return m * 3.281
#
# print(feet_to_meter(10.0))
# print(meter_to_feet(3.048))

# Task 4
# ''' Reminder that all the weights listed in this file ARE NOT a reflection
# of how your real grade will be broken down in this course. Always,
# refer to your syllabus for this information.
# '''
#
# def percentage(raw_mark: float, max_mark: float) -> float:
#     '''Return the percentage mark on a piece of work that received a mark of
#     raw_mark where the maximum possible mark is max_mark.
#     >>> percentage(15.0, 20.0)
#     75.0
#     >>> percentage(2.0, 20.0)
#     10.0
#     '''
#     return raw_mark / max_mark * 100
#
# def contribution(mark_as_percent: float, weight: float) -> float:
#     '''Given a piece of work that earned mark_as_percent percent and was
#     worth weight marks in the marking scheme, return the number of marks it
#     contributes to the final course mark.
#     >>> contribution(50.0, 12.5)
#     6.25
#     >>> contribution(20.0, 10.0)
#     2.0
#     '''
#     return mark_as_percent * (weight / 100)
#
# def raw_contribution(raw_mark: float, max_mark: float, weight: float) -> float:
#     '''Given a piece of work where the student earned raw_mark marks out of a
#     maximum of max_marks marks possible, return the number of marks it
#     contributes to the final course mark if this piece of work is worth weight
#     marks in the course marking scheme.
#     >>> raw_contribution(13.5, 15.0, 10.0)
#     9.0
#     >>> raw_contribution(5.0, 15.0, 20.0)
#     6.666666666666666
#     '''
#     return raw_mark / max_mark * weight
#
# def assignments_contribution(a1: float, a2: float, a3: float) -> int:
#     '''NOTE: The type annotations are missing! Please add them.
#     Given raw marks a1, a2 and a3 for the three course assignments,
#     calculate the contribution to the final course grade.
#     Assume each assignment is marked out of 50.
#     The assignments are worth 5%, 12.5%, and 5%, respectively, so the
#     return value of this function has a max of 22.5.
#     >>> assignments_contribution(30.0, 32.0, 20.0)
#     13
#     '''
#     return int((a1 / 50 * 5) + (a2 / 50 * 12.5) + (a3 / 50 * 5))
# print(assignments_contribution(30.0, 32.0, 20.0))
#
# def prep_review_practice_contribution(prep_review: float, practice: float) -> int:
#     '''Given raw marks for prep and review (Sunday and Friday PCRS assignments)
#     and practice (clickers, PCRS practice, or labs), calculate the contribution
#     to the final course grade.
#     NOTE: Prep and Review is marked out of 27, and practice is marked out of 8.
#     The former has a contribution of 7.5%, and the latter has a contribution of
#     10%,
#     so the return value of this function has a max of 17.5.
#     >>> prep_review_practice_contribution(18.0, 8.0)
#     15
#     '''
#     return int((prep_review / 27 * 7.5) + (practice / 8 * 10))
# print(prep_review_practice_contribution(18.0, 8.0))
#
# def term_work_mark(assignments: float, prep_review: float, practice: float, midterm: float) -> float:
#     '''Given the contribution of:
#     assignments (out of 22.5)
#     prepare and review (out of 7.5)
#     practice (out of 10)
#     and midterm (as a percentage),
#     return the term mark grade.
#     NOTE: the midterm is worth 30%, so the returned mark represents a mark out of
#     70.
#     >>> term_work_mark(16.0, 8.0, 5.0, 80.0)
#     53.0
#     '''
#     return (assignments + prep_review + practice + (midterm / 100 * 30))
# print(term_work_mark(16.0, 8.0, 5.0, 80.0))
#
# def exam_required(term_work: float, desired_grade: int) -> float:
#     '''Given a term work mark of term_work representing 70% of the points in the
#     grading scheme, calculate and return the percentage required on the exam for
#     the final mark to be desired_grade.
#     >>> exam_required(46.0, 82)
#     120.0
#     '''
#     return ((desired_grade - term_work) / 30 * 100)
# print(exam_required (46.0, 82))

# Task 5
# Research the syntax needed to have one of your function parameters be another function, and write a function that takes one
# input, two other functions and returns True or False whether the two functions return the same result on the given input.
# 255, 192, 203 - Pink
# 255, 182, 193 - Light Pink
# 170, 51, 106 - Dark Pink
#
# def is_light_or_dark(red: int, green: int, blue: int) -> bool:
#     """Return whether the colour meets our light-pink rule."""
#     return red == 255 and green <= 200 and blue <= 200
#
# def is_pink(red: int, green: int, blue: int) -> bool:
#     """Return whether the colour is exactly RGB (255, 192, 203)."""
#     return red == 255 and green == 192 and blue == 203
#
# def same_result(colour: tuple[int, int, int], function1, function2) -> bool:
#     """Return whether both functions return the same result for colour."""
#     return function1(*colour) == function2(*colour)
#
# same_result((255, 192, 203), is_light_or_dark, is_pink)

#Lab 3
# 1. my height is a float variable representing your current height in meters.
# a. Write a Python statement that assigns a Boolean variable tall the value of True if and only if I am at least 3.2
# meters tall
# def is_tall(my_height):
#     tall = False
#     if my_height >= 3.2:
#         tall = True
#     return tall
# print(is_tall(2.0))


# 2. min height is another float variable representing the minimum height I need to be allowed on the rollercoaster (This
# values changes depending on which rollercoaster I want to attend).
# b. Write a Python statement that creates a Boolean variable close that is True if and only if my current height is above
# the minimum height, but is dangerously close (i.e. within 0.04 of the minimum height).
# def is_allowed(my_height):
#     min_height = 1.7
#     close = True
#     if my_height >= min_height and my_height - min_height <= 0.04:
#         close = True
#     return close
# print(is_allowed(1.7))

# 3. A student may get into CSC311 (Intro to Machine Learning) if they have a GPA of 2.0 or higher, and if they have taken
# at least one of MAT223 or MAT240 (These are not the real requirements). g is a float variable representing my
# current GPA, and MAT223 and MAT240 are Booleans: MAT223 is True if and only if I have taken MAT223, and MAT240 is
# True if and only if I have taken MAT240.
# c. Write a Python expression with the variables g, MAT223 and MAT240 that evaluates to True if I can take CSC311, and
# to False otherwise. Note: you cannot use an “if” statement here; you are explicitly being asked for an expression,
# not a statement!
# def can_take_course(g, mat223, mat240):
#     can = False
#     if g >= 2.0 and mat223 == True and mat240 == True:
#         can = True
#     return can
# print(can_take_course(2.0, True, False))

# 4. Now, assume that we do not know what my actual GPA is (we do not have the float g but we have a Boolean variable b
# that represents whether my GPA is at least 2.0.
# d. Write another expression, using b, MAT223, and MAT240: it should evaluate to True if I can take CSC311, and to
# False otherwise.
# def can_take_with_no_g(b, mat223, mat240):
#     can = False
#     if b == True and mat223 == True and mat240 == True:
#         can = True
#     return can
# print(can_take_with_no_g(True, True, True))
#
# str1 = 'fourtyseven'
# str2 = 'sixtyfive'
# if len(str1) > len(str2):
#     print(str1)
# else:
#     print(str2)
#

# Practical Week 4, October 6
# 1. Determine whether a string ends with the letter “c”.
# s = "abcdefg"
# a = s.endswith("c")
# print(a)

# 2. Determine whether a string contains only letters.
# f = "abcdefg"
# b = f.isalpha()
# print(b)

# 3. Replace every instance of the character “a” with “b”.
# g = "abcdefg"
# c = g.replace("a", "b")
# print(c)

# 4. Given a string composed only of numbers, pad it with zeros on the right side so that it is exactly 6 digits long.
# j = "123"
# e = j.ljust(6, '0')
# print(e)

# 5. Determine whether a string contains only uppercase letters.
# h = "abcdefg"
# d = h.isupper()
# print(d)

# 6. Remove all trailing zeroes from a string composed only of numbers.
# k = "123000"
# i = k.rstrip('0')
# print(i)


# for char in s:
#     print(char)
# s = 'superconductivity'
# for index in range(len(s)):
#     r = s[index] + ','
#     if index == len(s) - 1:
#         r = s[index]
#     print(r, end='\t')


#  character in s and its index on the same line
# s = 'parsimonious'
# for index in range(len(s)):
#     print (s[index], index, end=' ')
#
# #  only the characters in s that are at odd indices.
# for index in range(len(s)):
#     if index % 2 == 1:
#         print(s[index])


# def shorter(s1, s2): Given two strings s1 and s2, return the length of the shorter string.
# string_one = "October"
# string_two = "September"
# def shortest(string_one, string_two):
#     return string_one if len(string_one) < len(string_two) else string_two
# print(shortest(string_one, string_two))


# def later(s1, s2): Given two strings s1 and s2 made up of lowercase letters, return the string that
# would appear later in the dictionary

# string_one = "year" # 121
# string_two = "decade" # 100
#
# if string_one > string_two:
#     print(string_one)
# else:
#     print(string_two)

# dictionary = ["month", "year", "day", "half_of_day", "decade", "century"]
# def later(string_one, string_two):
#     if string_one in dictionary and string_two in dictionary:
#         one = dictionary.index(string_one)
#         two = dictionary.index(string_two)
#         return string_one if one > two else string_two
#     return -1
# print(later(string_one, string_two))


#def without_letter(s, char): Given string s and a single-character string char, return the length
# of s if char was not in it. Remember that you may not use str.count()
# s = "banana"
# char = 'a'
# def without_letter(s, char):
#     leg = 0
#     for i in s:
#         if i != char:
#             leg = leg + 1
#     return leg
# print(without_letter(s, char))


# def remove_character(s, char): Given string s and a single-character string char, return a string consisting of
# s without any occurences of char.
# s = 'November'
# char = 'o'
# def remove_character(s, char):
#     see = ''
#     for i in s:
#         if i != char:
#             see = see + i
#     return see
# print(remove_character(s, char))


# Given string s and single-character string ch, return the index of the last
# occurrence of ch in s. For example, where(‘abc’, ‘b’) should return 1.
# If ch is not in s, return -1.
# Remember that you may not use str.find() or str.index() or any other string method.
# s = 'Spanish, Madrid'
# ch = 'a'
# def where(s, ch):
#     l_index = -1
#     for index, letter in enumerate(s):
#         if letter == ch:
#             l_index = index
#     return l_index
# print(where(s, ch))

# 21/10/26
# Practical
# 1
names = ['Bob', 'Hans', 'Zahara', 'Amitabha', 'Dov', 'Maria']
print(names[4:1:-1])
print(names[1:2])
print(names[:3])

#2
# Given a list L and a value v, write an expression that removes the first occurrence of v from L.
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
v= 1
L.remove(v)

# 3
# Write an expression that adds the string "What’s up?" to the front of the list ["Nothing much."]
L1 = ["Nothing much."]
L1.insert(0, "What's up?")

# 4
# Write code that turns [1, 3, 97, 0.1, -3.4, 86.95, -102] into [97, 86.95, 3, 1, 0.1, -3.4, -102].
L2 = [1, 3, 97, 0.1, -3.4, 86.95, -102]
L2.sort(reverse=True)

# 5
# Open a new file and in it write a function every_second that takes a list as a parameter and returns a new list that
# contains every second element of the original list, starting at index 0.
def every_second(L3: list) -> list:
    result = []
    for index in range(0, len(L), 2):
        result.append(L3[index])
    return result
every_second([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

# 6
# In the same file write a second function every_ith that takes a list L and an integer i as parameters and returns a list
# consisting of every ith element of L, starting at index 0.
def every_ith(L4: list, i: int) -> list:
    result = []
    for index in range(0, len(L4), i):
        result.append(L[index])
    return result
every_ith([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 5)

# 7
# Now that you have every_ith available, write a third function every_second_revisited that has the same behaviour as
# every_second but is only a single line of code.
def every_second_revisited(L5: list) -> list:
    return every_ith(L, 2)
every_second_revisited([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

# 2
# Print each element of list L on the same line.
def print_list(L: list) -> None:
    for item in L:
        print(item, end=' ')
    print()

# Print the elements of list L that occur at odd indices.
def print_list_odd(L: list) -> None:
    for index in range(1, len(L), 2):
        print(L[index])

# Print the elements of list L that occur on even indices from the end
# of the list to the front on the same or separate lines.
def print_list_reverse_even(L: list) -> None:
    for index in range(len(L) - 1, -1, -1):
        if index % 2 == 0:
            print(L[index])

# Sum the elements of the list L of ints, starting from the back of list,
# until the total is over 108 or the end of the list is reached, and return the
# sum at that point (as an int).
def sum_elements(L: list[int]) -> int:
    total = 0
    index = len(L) - 1
    while index >= 0 and total <= 108:
        total += L[index]
        index -= 1
    return total

# Return True iff list L contains at least three adjacent elements with the same value. For
# example, duplicates([1,1,1,2]) returns True and duplicates([1,2,1,1]) returns False
def duplicates(L: list) -> bool:
    for index in range(len(L) - 2):
        if L[index] == L[index + 1] and L[index + 2]:
            return True
    return False

# 4
pets = [["Shoji", "cat", 18], ["Hanako", "dog", 15], ["Sir Toby", "cat", 10],
["Sachiko", "cat", 7], ["Sasha", "dog", 3], ["Lopez", "dog", 13]]

# 1
# Write a for-loop that prints each list from list pets two lines apart (Only use one print statement).
for pet in pets:
    print(pet, end='\n\n')

# 2
# Write a for-loop that prints the first element of each inner list in list pets on a separate line.
for pet in pets:
    print(pet[0])

# 3
# Write a for-loop that computes the number of cats in pets.
cats = 0
for pet in pets:
    if pet[1] == 'cat':
        cats += 1
print(cats)

# 4
# Write a for-loop that computes the average of the ages of the animals in pets. Ages are the third element of the inner lists.
total = 0
for pet in pets:
    total += pet[2]
average = total / len(pets)
print(average)

# 5
# Write a function nested_lengths that takes a list L as a parameter and returns a list of the lengths of the sublists.
def nested_lengths(L: list) -> list:
    result = []
    for item in L:
        if isinstance(item, list):
            result.append(len(item))
        else:
            result.append(0)
    return result
print(nested_lengths([[1, 2], ['a', 'b', 'c']]))
print(nested_lengths([[1], 5, [], 'testing']))

# What is one thing you learned this week that sparked
# your curiosity? Why are you grateful for this learning experience?
# I would suppose that nailing squueze theorem this week was the most inspiring thing to work on.
# All those various functions of sin like sin(xx)/x can be illustrated and bounded with just 1/x.
# That was very beautiful mathematics considering the pase of MAT137 with weekly tests. I am grateful
# because it clicked very well and I wrote many proofs in just few minutes after introduction of the
# topic. Also, today I proved differentiation without quotient rule by limit definition. It was quite
# fresh because in AP calc BC it was not even thinkable. Lastly, computed lim h -> 0 f(a-h)-f(a)/-h
# to use it in my proof which I never previously calculated, instead used the +h version.

# 7
# >>> rotate([
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]
# ])
# return
# [
# [7, 4, 1],
# [8, 5, 2],
# [9, 6, 3]
# ]
def rotate(L5: list) -> list:
    L6 = []
    for column in range(len(L5[0])):
        row = []
        for index in range(len(L5) - 1, -1, -1):
            row.append(L5[index][column])
        L6.append(row)
    return L6
L5 = [
    [0, 1, 0],
    [20, 0, 5],
    [0, 10, 0]
]
result = rotate(L5)
print(*result, sep="\n")
