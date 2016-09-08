# Template for code submission
# name : Nabil Alhassani
# email : nda11@pitt.edu
# date :septemper/8th
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# Description:Starting with Python, Chapter 2,
# Notes:
# any notes to the instructor and/or TA goes here
# ...and now let's program with Python

# exercise 6
# This program asks the user to enter the amonut purchases
#the program should compute the state and county tax
#input amonut_price
amount_price = float(input('enter the price for your purches:'))

#set state_tax , county_tax and total tax
county_tax = 0.025
state_tax=0.05
total_tax = county_tax + state_tax
#set total_cost
total_cost = amount_price * (1+total_tax)
#Display the amont_price
print("the total cost is $",total_cost)
print("the purchase amount price was $",amount_price)
print ("the county tax was $",county_tax)
print ("the state tax was $",state_tax)
print ("the total tax was $",total_tax)

