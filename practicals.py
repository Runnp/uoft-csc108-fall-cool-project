#print(3000-711)
#print(49/8)
#print(270//3)
#print(270%3)

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
def leetcodes_answered(num_weeks: int, questions_per_week: int) -> int:
    '''Return the total number of leetcode questions done over num_weeks
    where in each week questions_per_week were answered
    >>> leetcodes_answered(2, 30)
    60
    >>> leetcodes_answered(1, 8)
    8
    '''
    return num_weeks * questions_per_week
# two of us are doing leetcode but at different rates and different amounts of time
person_a = leetcodes_answered(2, 8)
person_b_rate = 30
person_b = leetcodes_answered(1, person_b_rate)
grand_total = person_a + person_b
print("With the two of us combined, we will have done", grand_total, "questions")

# Task 2
def cookies_needed(adults: int, teens: int, children: int) -> int:
    '''Return the number of cookies needed to
    feed this number of adults, teens and children.
    Each adult eats two, each teen six, and each child three.
    >>> cookies_needed(2, 3, 1)
    25
    '''
    adults_cookies = 2
    teen_cookies = 6
    child_cookies = 3
    return adults_cookies * adults + teen_cookies * teens + child_cookies * children
#
def is_multiple_of_7(x: int) -> bool:
    '''Return True iff 7 divides x without a remainder.
    >>> is_multiple_of_7(15)
    False
    >>> is_multiple_of_7(7)
    True
    '''
    return x % 7 == 0
#
def is_multiple(x: int, y: int) -> bool:
    '''Return True iff y divides x without a remainder.
    >>> is_multiple(15, 3)
    True
    >>> is_multiple(7, 2)
    False
    '''
    return x % y == 0


# Task 3
def feet_to_meter(f: float) -> float:
    '''Return the number of meters equivalent to f feet.
        >>> feet_to_meter(10.0)
        3.047851264858275
    '''
    return f / 3.281

def meter_to_feet(m: float) -> float:
    '''Return the number of feet equivalent to m meters.
        >>> meter_to_feet(3.048)
        10.000488
        '''
    return m * 3.281

print(feet_to_meter(10.0))
print(meter_to_feet(3.048))

# Task 4
''' Reminder that all the weights listed in this file ARE NOT a reflection
of how your real grade will be broken down in this course. Always,
refer to your syllabus for this information.
'''

def percentage(raw_mark: float, max_mark: float) -> float:
    '''Return the percentage mark on a piece of work that received a mark of
    raw_mark where the maximum possible mark is max_mark.
    >>> percentage(15.0, 20.0)
    75.0
    >>> percentage(2.0, 20.0)
    10.0
    '''
    return raw_mark / max_mark * 100

def contribution(mark_as_percent: float, weight: float) -> float:
    '''Given a piece of work that earned mark_as_percent percent and was
    worth weight marks in the marking scheme, return the number of marks it
    contributes to the final course mark.
    >>> contribution(50.0, 12.5)
    6.25
    >>> contribution(20.0, 10.0)
    2.0
    '''
    return mark_as_percent * (weight / 100)

def raw_contribution(raw_mark: float, max_mark: float, weight: float) -> float:
    '''Given a piece of work where the student earned raw_mark marks out of a
    maximum of max_marks marks possible, return the number of marks it
    contributes to the final course mark if this piece of work is worth weight
    marks in the course marking scheme.
    >>> raw_contribution(13.5, 15.0, 10.0)
    9.0
    >>> raw_contribution(5.0, 15.0, 20.0)
    6.666666666666666
    '''
    return raw_mark / max_mark * weight

def assignments_contribution(a1: float, a2: float, a3: float) -> int:
    '''NOTE: The type annotations are missing! Please add them.
    Given raw marks a1, a2 and a3 for the three course assignments,
    calculate the contribution to the final course grade.
    Assume each assignment is marked out of 50.
    The assignments are worth 5%, 12.5%, and 5%, respectively, so the
    return value of this function has a max of 22.5.
    >>> assignments_contribution(30.0, 32.0, 20.0)
    13
    '''
    return int((a1 / 50 * 5) + (a2 / 50 * 12.5) + (a3 / 50 * 5))
# print(assignments_contribution(30.0, 32.0, 20.0))

def prep_review_practice_contribution(prep_review: float, practice: float) -> int:
    '''Given raw marks for prep and review (Sunday and Friday PCRS assignments)
    and practice (clickers, PCRS practice, or labs), calculate the contribution
    to the final course grade.
    NOTE: Prep and Review is marked out of 27, and practice is marked out of 8.
    The former has a contribution of 7.5%, and the latter has a contribution of
    10%,
    so the return value of this function has a max of 17.5.
    >>> prep_review_practice_contribution(18.0, 8.0)
    15
    '''
    return int((prep_review / 27 * 7.5) + (practice / 8 * 10))
# print(prep_review_practice_contribution(18.0, 8.0))

def term_work_mark(assignments: float, prep_review: float, practice: float, midterm: float) -> float:
    '''Given the contribution of:
    assignments (out of 22.5)
    prepare and review (out of 7.5)
    practice (out of 10)
    and midterm (as a percentage),
    return the term mark grade.
    NOTE: the midterm is worth 30%, so the returned mark represents a mark out of
    70.
    >>> term_work_mark(16.0, 8.0, 5.0, 80.0)
    53.0
    '''
    return (assignments + prep_review + practice + (midterm / 100 * 30))
# print(term_work_mark(16.0, 8.0, 5.0, 80.0))

def exam_required(term_work: float, desired_grade: int) -> float:
    '''Given a term work mark of term_work representing 70% of the points in the
    grading scheme, calculate and return the percentage required on the exam for
    the final mark to be desired_grade.
    >>> exam_required(46.0, 82)
    120.0
    '''
    return ((desired_grade - term_work) / 30 * 100)
# print(exam_required (46.0, 82))

# Task 5
# Research the syntax needed to have one of your function parameters be another function, and write a function that takes one
# input, two other functions and returns True or False whether the two functions return the same result on the given input.
# 255, 192, 203 - Pink
# 255, 182, 193 - Light Pink
# 170, 51, 106 - Dark Pink

def is_light_or_dark(red: int, green: int, blue: int) -> bool:
    """Return whether the colour meets our light-pink rule."""
    return red == 255 and green <= 200 and blue <= 200

def is_pink(red: int, green: int, blue: int) -> bool:
    """Return whether the colour is exactly RGB (255, 192, 203)."""
    return red == 255 and green == 192 and blue == 203

def same_result(colour: tuple[int, int, int], function1, function2) -> bool:
    """Return whether both functions return the same result for colour."""
    return function1(*colour) == function2(*colour)

same_result((255, 192, 203), is_light_or_dark, is_pink)
