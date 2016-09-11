# Template for code submission
# name : Nabil Alhassani
# email : nda11@pitt.edu
# date :septemper/11th
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# Description:Starting with Python, Chapter 2,
# Notes:
# any notes to the instructor and/or TA goes here
# ...and now let's program with Python

# exercise 10#
# This program asks the user how many cookies he or she wants to make
# Then displays the quantity needed for each ingredient for the specified number of cookies.

#Frist:


# input many cookies you want to make
number_of_cookies=input('Enter number of cookies you want to make:')

#set cookie recipe for cookies
# sugar,buttes,flour per 48 cookies
sugar=300
buttes=240
flour=330

#calculation A cookie recipe for cookies
# sugar,buttes,flour
sugar=300* number_of_cookies/48
buttes=240*number_of_cookies/48
flour=330*number_of_cookies/48



#Display the result
print('This is your recipe:',sugar,'gram of sugar,',buttes,'gram of buttes''and',flour,'gram flour')
