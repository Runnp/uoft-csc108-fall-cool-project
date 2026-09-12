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