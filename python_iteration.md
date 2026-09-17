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
