so, I know Python for years but it is important to repeat and do not mix it with Java lingo in my head cause last year
I did a bunch of programming for AP Computer Science A

String is designed like:
name = "John"
/n
\"
phrase = phrase + "is old"
print(phrase.upper())
print(len(phrase))
print(phrase[0]) - "J"
print(phrase.index("o")) - "7"
print(phrase.replace("John", "Mark"))

Integer, Decimal numbers:
n = 5
m = 5.33
print(10 % 3) - 1
print(abs(-5))
print(pow(3,2)) - 3^2 = 9
print(max(4,5) - 5
print(round(3.7))

from math import *
print(floor(4.5) - 4
print(ceil(4.5) - 5
print(sqrt(25)) - 5


Data Variable Conversion:
num = 5
print(str(num))




Boolean:
isCool = True


Notes from Class:
* 
* What value does round(1234.5678, -2) produce?
* 1235
* 1200
* 1200.0 - c
* 1235.0
* c - correct
* 
* What value does round(2.5) produce?
* 2 - a
* 2.0
* 3
* 3.0
* a - correct, even stays, but if odd it increases

* 
* Syntax
*  a, b = b, a 
* will swap the variables all in one line
* 
* Consider this code:
* apple = banana When the code above is executed, what type of error occurs?
* SyntaxError
* NameError
* 
* Consider this code:
*  '5' + 5 
* When the code above is executed, what type of error occurs?
* TypeError

* 
* Which of the following is an appropriate definition for the function double that returns two times the number it is passed?
* def double(x):
*     return 2 * x
* 
* grade = 80
* not (grade >= 50) - not true - false
* also not (grade < 50) works
* 
* When history_grade is 85, gives a True statement because we have or, either one side if true makes the whole expression true 
* (math_grade > 50) or (history_grade > 50)
* 
* Consider this expression: ‘ba’+ ‘na’ * 2 + ‘muffin’. What does it evaluate to?
* ‘bana2muffin’
* ‘bananamuffin’ - correct, since * 2 means “nana”
* 
* print(str(1), 'st love') - 1 st love
* Comma will result in a space
* 
* print('What\'s up?\nDoc')
* What's up?
* Doc
* 
* From input(), the data you receive is always in str unless you did not convert
* 
* The Type Contract describes the types of the parameters and return value. Select the correct Type Contract for this function.
* (str) -> int - correct
* (int) -> str
* (string) -> integer
* (integer) -> string

* def count_vowels(word: str) -> int:
*     """Count the vowels in the string.
*     """
* Identify the problem(s) with the Description in the docstring above.
* It doesn't say what the function returns. - correct
* It's too short.
* It doesn't mention the type of the parameter.
* It doesn't mention the parameter by name. - correct
* 
* Assume you already have a function convert_to_celsius. That function has one parameter representing a temperature in Fahrenheit and returns that temperature in Celsius. In the same file, we define another function:
* def colder_temperature(temp1: float, temp2: float) -> float:
*     """Return the colder of the two temperatures, temp1 (degrees Celsius)
*     and temp2 (degrees Fahrenheit), in degrees Celsius.
*     """
* Which of the following is the best choice for the function body?
* temp2_celsius = convert_to_celsius(temp2)
* return min(temp1, temp2_celsius)
* correct cause the temp 1 is already in celsius
* 
* Select the code fragment(s) that result in a SyntaxError.
* "He said, "Yes!"" - incorrect
* '"Once upon a time...", she said.'
* '3\' - incorrect
* 'That\'s okay'
* 
* What is the first step of the Design Recipe?
* Header
* Test
* Examples - correct
* Code
* 
* What is the last step of the Design Recipe?
* Code
* Header
* Test - correct
* Examples
* 
* print("A\t1")
* A 1
* print("B\t2")
* B 2
* /t acts like a one space place
* 
* print("\"I am a slow walker, but I never walk back.\" - Abe Lincoln")
* "I am a slow walker, but I never walk back." - Abe Lincoln
* 
* print("You say, \"Goodbye\", I say, \"Hello\"")
* You say, "Goodbye", I say, "Hello"
* print("Hello ALIEN!".lower())
* hello alien!
* 
* a = "Hello".upper()
* b = "WoRlD".lower()
* print(a + " " + b + "!")
* HELLO world! - output
* 
* a = "Hello ".strip()
* b = " world!".strip()
* print(a + b)
* Helloworld! - output
* 
* Just reloading the website oftentimes helps to read the code:
* def format_name(first_name: str, last_name: str) -> str:    
*     return(last_name + ", " + first_name)
* 
* def to_listing(first_name: str, last_name: str, num: str) -> str:
*     """Return a string in the format "LAST_NAME, 
*     FIRST_NAME: PHONE_NUMBER", where LAST_NAME, FIRST_NAME, and 
*     PHONE_NUMBER are replaced by last_name, first_name, and num.
* 
*     >>> to_listing('David', 'Cohen', '12345')
*     'Cohen, David: 12345'
*     """
*     return format_name(first_name, last_name) + ": " + num # Implement your function here.
* * 12/09/26
* Select the legal Python name(s) below.
happy_day
happy!day?
18happy_day
happy_45day
* 1, 4 are correct
* You cannot start a variable with a number
* 
* Consider this code:

round(45.342, 2)
What value does the expression above produce?
* 45.342
* 45.34
* 45.3
* 45
* The correct answer is 45.34, the number 2 in the brackets means how many digits we are leaving after a period
* Consider this code:

data = 3
data2 = 7.5
result = min(data, data2)
 Select the phrase that describes data in the third line.
* a parameter
* an argument
* a function name
* The correct answer is an argument
* 
* 14/09/26
* Lecture Notes
* Test is October 1st
* True is a type of Boolean
* True + 1, Boolean is a subclass
* Results in 2 = 1 + 1
* bool(8) - True
* bool(-100.25) - True
* bool(0) - False

* De Morgan’s Laws
* not(a and b) ‎ = = not a or not b
* You do not draw only overlap, between a and b
* 
* not(a or b) ‎ = = not a and not b
* You draw everything except the two circles and overlap
* 
* Short Circuits
* a and b and c, if a is true, b is false, but c is not reached
* There is no point of calculating it since it does not get to c, it stops at b
* a or b or c, where a is false, b is true, it will not reach c still but it will be true because of b

* 
* True or 1/0 - will return True even if 1/0 is Error
* False or 1/0 - ZeroDivisionError
* True or ahahhaahhaha - will do Lazy Evaluation and return True
* True or ! - will return SyntaxError: invalid syntax because of “!”
* 
* True or False or False
* (True or False) and False - order of operation
* 
* True
* False
* True
* False
* 
* False - False and True
* True - False or True - True and False - False - False or False - False or True
* The “and” is in higher priority than “or”
* False and False, you do not have to look at all other things after and it will do Lazy Evaluation and give you False
* 
* Hand Tracing
* True
* True
* True and True - True
* 
* Simplify
* not(b or not a or not b) - for Wednesday
* 
* b or not a
* not a or not b ‎ =  not (a and b)
* b or not (a and b)
* 
* not(b or not (a and b))

* 
* Simplify
* not(b or not a or not b) - for Wednesday
* not( (b or not a) or (not b) )
* not(b or not a) and not (not b) - flip or to and
* not(not b) - it is b
* not b and not (not a) and b
* not b and a and b
* a and b and not b
* a and False
* Therefore, False
* 
* not(b or not (a and b))
* not b and not(not(a and b))
* not b and (a and b)
* a and b and not b
* b and not b
* Therefore, False
* * 
* 16/09/26
* Lecture
* Functions:
* type()
* min(a, b, c)
* max(a, b, c)
* abs(a) - cannot put multiple arguments like (a, b, c)
* API sheet will be provided in midterm
* help(abs) - it returns the abs(x, /), meaning which it takes one argument
* dir(__builtins__) - dir gives a list of all built-in functions, very helpful
* import math
* function design recipe
* there is no 1-1 requirement

* 
* def[]f(x):
* [][][][]function statement
* indenting
* convention - verb noun so that others can follow ur code
* pythonic - like correct way of doin
* def f(x, y):
*     return x % y
* x = f (5, 2) - which is 1
* y = f (20, 7) - which is 6
* 
* return value = none, when using print
* return x = 3, return value = 9
* we aint able  reuse tha
* 
* -2 % 6 = 4
* 1
* def example(x):
*     print (2 * x) - will display 2
*     return 3 * x - it will not display on the screen
* * 
* def example(x):
*     print (1 * x)
*     return 3 * x 
*     print (2 * x)
* a = example (1)
* - will display only 1, cuz everything stops after return
* - will display only 3, first return then freezes
* 
* When nothing to return - will display None
* def area_Triangle(a, b, c):
*     return 1/2 * (a + b + c)


* 18/09/26
* Lecture
* x = (q * y) + r
* To find q, do -2 // 6.
* We know -2/6 is -0.33
* // does floor -1, q = -1
* def triangle_area(a: int, b: int, c: int) -> float
* No checking will take place
* We are all Adam
* Function: Docstrings
* args(): type,…
* Global scope
* Local scope
* Takes it off after return x
* Memory management
* Replace
* def foo():
*     x = 2
*     return x
* x
* NameError: name ‘x’ is not defined
* 
* text = "  abc  "
* print(len(text.strip()))
* - len(text.strip()) will result in just how many real letters does the text have,
* in this example only three letters, a b c namely, counted up to 3
* 
* x = 7
* def foo():
*     x = x + 2
*     return
* 
* foo()
* Local scope cannot add from Global scope
* Therefore, UnboundLocalError: local variable ‘x’
* msg = "banana"
* print(msg.count("an", 1, 4))
* - output 1
* 
* msg = "banana"
* print(msg.count("an", 1, 5))
* - output 2
* 
* Docstring
* >>> is_sorted("123")
* True
* >>> is_sorted("132")
* False
* You write inside the code
* 
* 19/09/26
* >>> bro = input("How many brothers do you have? ") 
* How many brothers do you have? 4
* >>> sis = input("How many sisters do you have? ")
* How many sisters do you have? 2
* >>> sibs = ' siblings!'
* Assuming the code above has been executed, choose the expression below that evaluates to: 6 siblings!
* (bro + sis) + sibs
* - 42 siblings! 
* str(int(bro) + int(sis)) + sibs
* - 6 siblings!
* str(int(bro + sis)) + sibs
* - 42 siblings!

* 
* s = 'Call Me Maybe'
* Select the expression(s) that produce 'e'.
* s[12] - True
* s[13]
* s[-0]
* s[-1] - True
* 
* Consider this code:
* >>> white_queen = "Jam tomorrow and jam yesterday - but never jam today."
* >>> white_queen.count("jam")
* 2
* The code above counts only lowercase occurrences of "jam". Below is the output of help(str.lower):
* lower(...)
*     S.lower() -> str
*     Return a copy of the string S converted to lowercase.
* Which expression produces the number of occurrences of "jam" ignoring letter case?
* white_queen.count("jam").lower()
* white_queen.lower().count("jam") - True
* white_queen.count("Jam".lower())
* 
* The math module has a function that finds the ceiling of a number (the smallest int value greater or equal to the number). Assuming that the math module has already been imported, write an expression that calls the ceiling function from math to find the ceiling of 84.2.
* Hint: In the Python shell, import math and then use dir and help on the math module to determine the name of the function that you need to use.
* math.ceiling(84.2)
* ceiling(84.2)
* math.ceil(84.2) - True
* 
* print(int(99.9) - will result in 99
* rint('hello', '-', 'how', '-', 'are', '-', 'you')
* will result in ‘hello - how - are - you’
* 
* SyntaxError: Select the code fragment(s) that result in a SyntaxError.
* 1)’yes\nno'
* 2)”yes
* no"
* 3)’’’yes
* no'''
* 4)’ yes
* no'
* The right answers are 2 and 4.
* 
* Select the expression(s) that produce True.
* 'as' in 'it happens'
* len('aabbcc') == 6
* 'do' in "don't"
* len('aabbcc') == 3
* The right answers are 2 and 3.
* 
* Select the expression(s) that produce True.
* 'apple'.upper() == 'APPLE'
* - True
* 'abc123'.isdigit()
* - False
* 'apple'.upper().isupper()
* - True
* 'apple'.upper().islower()
* - False
* 'abc123'.isalnum()
* - True
* '12.34'.isalnum()
* - False
- * Select the expression(s) that produce True when variable s refers to a str that is entirely alphabetic or entirely numeric, and that produce False if they are not entirely alphabetic and not entirely numeric.
* s.islower() or s.isupper()
* s.isalpha() and s.isnumeric()
* s.lower() or s.upper() or s.isdigit()
* s.isalpha() or s.isnumeric() - True
* The right answer is 4.
* 
* After the following assignment statement has been executed, which expression(s) produce the letter "g"?
* dance_style = "Gangnam"
* dance_style[-5]
* dance_style[-4] - True
* dance_style[2]
* dance_style[4]
* dance_style[-3]
* dance_style[3] - True
* The right answers are 2 and 6.
* 
* Considering this code:
* s = 'pineapple'
* Select the expression(s) that produce 'apple'.
* s[4:9]
* - apple
* s[-5:]
* - apple
* s[-5:-1]
* - appl
* s[5:9]
* - pple
* s[4:len(s)]
* - apple
* s[5:]
* - pple
* The right answers are 1, 2, and 5
* 
* Consider this code:
* s = 'Jacqueline'
* You know that the slicing operation s[1:4] will produce the string 'acq'. The slicing operation has an optional third parameter that determines the stride (or distance between characters) in the slice. For example, the slicing operation s[::2] will produce the string 'Jculn', which has every other character in 'Jacqueline'
* 
* Consider this code:
* s = 'Jacqueline' Select the expressions that produce 'aqeie'.
* s[0:0:2]
* s[::2]
* s[1:0:2]
* s[1::2] - True
* 
* Consider this code:
* s = 'Jacqueline' Select the expression(s) that produce the string 'enileuqcaJ'.
* s[::-1] - True
* s[::]
* s[::-2]
* s[0:-1:-2]
* 
* Consider this code:
* s = 'Jacqueline' Select the expression(s) that produce the string 'eieqa'.
* s[::-1]
* s[-1:0:-2] - True
* s[::-2] - True
* s[0:-1:-2]
* 
* Consider this code wish = 'Happy Birthday' After the code above is executed, which of the following expressions produces 'happy birthday'?
* wish[0].lower() + wish[6].lower()
* wish.swapcase()
* wish[0].lower() + wish[1:6] + wish[6].lower() + wish[7:] - True
* wish.lower() - True
* H
* Consider this code: robot = 'R2D2' Assuming the code above has been executed, select the expression(s) that produce True.
* robot.isupper() - True
* robot.isalpha()
* robot.isalnum() - True
* robot.isdigit()
* 
* Consider this code:
* lyrics = '''O Canada!
* Our home and native land!
* True patriot love in all of us command.''' Select the expression that produces the index of the second exclamation mark.
* lyrics.find('!')
* lyrics.find('!').find('!')
* lyrics.find('!', lyrics.find('!'))
* lyrics.find('!', lyrics.find('!') + 1) - True
* 
* Considering this code:
* s = 'carrot' Select the expression(s) that produce 'car'.
* s[:3]      - car
* s[-1:3]  - 
* s[-6:3] - car
* s[0:4]   - carr
* s[-6:-3] - car
* s[-6:4]   - carr
* 
* Consider this code:
* prefix = 'mad' What does the expression prefix[:1] + prefix[1:3] + prefix[-2] + prefix[0] produce?
* 'madam
* 'madma'
* 'adama'
* 
* Complete the function body below so the return statement executes correctly according to the docstring description and examples.
def swap_ends(message: str) -> str:
    """Return a new string that is message with the first and last
    characters swapped.
    
    Precondition: len(message) >= 2
    
    >>> swap_ends('cat')
    'tac'
    >>> swap_ends('breakfast for dinner!')
    '!reakfast for dinnerb'
    """
    last_char = message[-1]
    first_char = message[0]
    middle = message[1: len(message) - 1]
    return last_char + middle + first_char
* Select the code fragment(s) that evaluate(s) to True.
* 'how are you?'.isspace()
* '   Hi!   '.strip() == 'Hi!    '
* 'hello'.rfind('l') == 3      - True
* '007B!'.isupper()            - True
* 
* Complete this function according to its docstring description.
def upper_lower(s: str) -> bool:
    """Return True if and only if there is at least one alphabetic character
    in s and the alphabetic characters in s are either all uppercase or all
    lowercase.
    
    >>> upper_lower('abc')
    True
    >>> upper_lower('abcXYZ')
    False
    >>> upper_lower('XYZ')
    True
    """
    return s.isupper() or s.islower()


* 21/09/26
* Lecture
* Choosing a dataset for Assignment Phase 0
* To work with data, analysis and conclusions
* .csv

* 
* x = 7
* def foo():
*     x = x + 2
*     return x
* x  = x + foo(x)
* print(x)
* - will result in 16
* 
* import doctest
* def area_rectangle(length: float, width: float) -> float
*     >>>area_rectangle(1.0,5.0)
*     5.0
*     >>>area_rectangle(1.5,10.0)
*     15.0
*     >>>area_rectangle(1.0,1.0)
*     1.0
*     return length * width
* doctest.testmod()
* * 
* - doctest allows us to verify our code results
* “””Description of function””” - description
* header - description - use cases - body - return statement
* 
* def cookies(adults: int, teens: int, children: int) -> int:
*     “””Cookies for everyone”””
*     >>>(5, 2, 1)
*     20    
*     return (2 * adults + 3 * teens + 4 * children)

* 
* def scholarship(cgpa: float, year_of_study: int) -> float:
*     “””Requirements for being eligible for a scholarship are having CGPA above 3.7 and studying in 2 or 3 year of study”””
*     >>>(3.8, 2)
*     True
*     >>>(3.5, 3)
*     False
*     if (cgpa > 3.7):
*         if (year_of_study == 2 or year_of_study == 3):
*             return True
*         else: return False
*     else:
*         return False
* 
* scholarship(3.8, 1)
* - False
* scholarship(4.0, 2)
* - True

* 23/09/26
* Lecture
* id(x)
* id(y)
* Strings are saved in different IDs
* They are recreated and are immutable
* 
* “a” < “aa” - True
* “b” < “aa” - False
* “abba” < “a” - False
* Based on UniCode
* “Abba” < “a” - True
* “aZ” < “aa” - True
* 
* int(“string”) - Error
* lex(“word”) - 4
* return “str” in “string” - True
* int(“h”) - Error
* ord(“h”) - will return UniCode
* 
* x = "hello world”
* len(x) = 11
* x[len(x)] - IndexError: string index out of range
* 
* hello world - Backwards will begin at -1
* x[-1] = ‘d’
* 
* x = "0123456789"
* x[-1] == x[len(x)-1]
* True
* 
* x[3:]
* “3456789”
* 
* x[3:-1]
* “345678”
* 
* x[0:-1:2]
* “02468”
* 
* x[1:-3:3]
* “14”
* 
* x[::-1]
* “9876543210”
* 
* 3456789
* 345678
* 02468
* 14
* 9876543210
* 
* return input_str ‎ = = input_str[::-1]
*  
* 23/09/26
* Independent Study
* Consider this code:
* return temp == 22.5 Select the code fragment(s) that are equivalent to the one above.
* if temp == 22.5:
*     return True

* if temp == 22.5:
*     return True
* else:
*     return False


* if temp == 22.5:
*     return True
* elif temp != 22.5:
*     return False

* if temp == 22.5:
*     return True
* return False
* The correct answers are 2, 3, and 4
* 
* 
* The trick: separate ifs all get checked; an if/elif chain stops after its first true condition.
* Imagine both grades are 80:
* if grade1 >= 50:
*     num_passed = num_passed + 1
* if grade2 >= 50:
*     num_passed = num_passed + 1
* Correct  — two independent checks, each adding 1: if grade1 >= 50:    num_passed = num_passed + 1if grade2 >= 50:    num_passed = num_passed + 1 The count goes 0 → 1 → 2.
* * 
* Incorrect  — the first condition is true, so the elif is skipped. It counts only 1, even when both courses passed.
* 
* Incorrect  — it initially sets the count to 2, but the next independent ifs overwrite it with 1. The count goes 0 → 2 → 1 → 1.
* 
* if grade1 >= 50 and grade2 >= 50:
*     num_passed = 2
* elif grade1 >= 50:
*     num_passed = 1
* elif grade2 >= 50:
*     num_passed = 1
* Correct  — it first checks whether both passed. If so, it sets 2 and skips the remaining branches. Otherwise, it checks whether either individual course passed and sets 1. If neither passed, the count stays 0.

* l our code for the function count_vowels (shortened for space):
* def count_vowels(s: str) -> int:
*     num_vowels = 0
*     for char in s: 
*         if char in 'aeiouAEIOU':
*             num_vowels = num_vowels + 1
*     return num_vowels What will happen when we pass the empty string as the argument (that is, count_vowels(""))?
* 
* The for loop body will not execute, and num_vowels will continue to refer to 0.
* * 
* The for loop body will execute 1 time, with char referring to "". The if condition will be True, and num_vowels will then refer to 1.
* 
* An error will be raised when Python tries to iterate through the empty string.
* The correct answer is 1
* 
* 
* Consider this code:
* digits = '0123456789'
* result = 0
* for digit in digits:
*     result = digit
* print(result) What is printed by the code above?
* 0
* 45
* 9
* 0123456789
* The correct answer is 3
* 
* digits = '0123456789'
* result = ''
* for digit in digits:
*     result = result + digit * 2
* print(result) What is printed by the code above?
* 0123456789
* 90
* 45
* 00112233445566778899
* The correct answer is 4
* 
* 
* def common_chars(s1: str, s2: str) -> str:
*     """Return a string containing all characters from s1 that appear at least
*     once in s2.  The characters in the result will appear in the same order as
*     they appear in s1.
* 
*     >>> common_chars('abc', 'ad')
*     'a'
*     >>> common_chars('a', 'a')
*     'a'
*     >>> common_chars('abb', 'ab')
*     'abb'
*     >>> common_chars('abracadabra', 'ra')
*     'araaara'
*     """
* * 
*     res = ''
* 
*     # BODY MISSING
* 
*     return res
* The correct answer:
*     for ch in s1:
*         if ch in s2:
*             res = res + ch
* 
