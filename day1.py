#!/usr/bin/python
# Author: shridhar gadekar
# Date: 



Price = "Python Learning"

print Price

type(Price)


price = 390

# to get the type of variable use 'type()' function
#type(price)
print "Type of price", type(price)

price = 4809.989
print price
print "Type of price", type(price)

# to get the address(memory) of variable use 'id()' function
id(Price)
print "address of Price", id(Price)
price3 = Price
id(price3)

print "address of price3", id(price3)

price3 = 43974
print "address of price3", id(price3)




#####  math

print 2 ** 8
print 2 * 8 
print 4 / 2
print 2 + 2
print 2 - 2


# Order of execution # PEMDAS = ParenthesisExponentialsMultiplicationDivisionAdditionSubtraction
# multiplication carries same weight as division
# in case both are on same line then order of execution is from left to right
# same is true for addition and subtraction
print 2 ** 8 * 4 / 4 + 44 - 44


print 100 / 2 * 3

# parenthesis always gets first preference

print 100 / (2 * 3 )

# to get floating point value output 

print 100.0 / (2 * 3 )


# to get the remainder  use 'modulus' operator
print "remainder of 100 / 16 :", 100 % 16

print " 100 / 6 is:", 100 / 6, "\t and Remainder is:", 100 % 6 








#####
# concatenation of strings is possible with '+' operator

print "first", "second"
print "first" + "second"
print "Hello World" * 3

#### 
# Collect input from user or terminal
# two methods available 1. input()  2. raw_input()
# input() is used for collecting numeric inputs
# raw_input() is used for collecting all types of inputs from terminal

# following will collect input from terminal with a message "what is your message" in variable 'message', 
message = raw_input("What is your name")

print "You typed", message


# following will collect integers with input()

some = input("provide any number:")
print message, "would get", some, "Million Dollars"



