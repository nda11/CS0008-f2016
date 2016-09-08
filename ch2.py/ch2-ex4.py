# Template for code submission
# name : Nabil Alhassani
# email : nda11@pitt.edu
# date :septemper/7th
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# Description:Starting with Python, Chapter 2,
# Notes:
# any notes to the instructor and/or TA goes here
# ...and now let's program with Python

# exercise 4
# This program asks the user to enter the price of 5 items from
# the store and display the subtotal of sales
# and amonut of taxs
# Get input for the prices of 5 items from user
item1= float(input('Enter the price of item 1:'))
item2= float(input('Enter the price of item 2:'))
item3= float(input('Enter the price of item 3:'))
item4= float(input('Enter the price of item 4:'))
item5= float(input('Enter the price of item 5:'))
# calculate the subtotal
subtotal= item1+item2+item3+item4+item5
#print the subtotal
print('The subtotal of your items is:',subtotal)
#calculate sales tax and add it to subtotal
tax=subtotal*0.7
total=subtotal + tax
# display the total
print('the total amount of your items with tax is:',\
      format(total,',.2f'))
