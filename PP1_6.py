'''
	File Name: errors.py
	Author: Mr. Kalisz
	Date Created: March 29, 2019
	Date Last Edited: Sept 23, 2024
'''

# From input, recieve two integers from the user and add them together.  Output the result.
from math import floor


def q1():
  num1 = input("Input a number: ")
  num2 = input("Input a number: ")
  int1 = int(num1)
  int2 = int(num2)
  print (int1 + int2)

# From input recieve two integers.  Output the quotient rounded down.

def q2():
  (num6) = input("Input a number: ")
  (num9) = input("Input a number: ")
  banana = floor((int(num6))/(int(num9)))
  print(banana)

# Output the phrase "hello Mr. Kalisz have you seen my work yet?"

def q3():
  print("hello Mr. Kalisz have you seen my work yet?")

# From input recieve two numbers (can be decimal fractions).  
# Output their result multiplied together.  Then round down to the nearest whole number

def q4():
  number1 = float(input("Input a number: "))
  number2 = float(input("Input another number: "))

  print (int(number1 * number2))
  

# q1()
# q2()
# q3()
# q4()
