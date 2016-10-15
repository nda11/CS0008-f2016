# name : Nabil Alhassani
# email : nda11@pitt.edu
# date :septemper/11th
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# Description:Starting with Python, Chapter 2,
# Notes:
# any notes to the instructor and/or TA goes here
# ...and now let's program with Python

# exercise 3
# Many financial experts advise that property owners should insure
# their homes or buildings for at least 80 percent of the amount
# it would cost to replace the structure.  Write a program that
# asks the user to enter the replacement cost of a building and
# then displays the minimum amount of insurance he or she should
# buy for the property.


def main():
    # Ask for the replacement cost of the insured building.
    replacement_cost = input('Enter the replacement cost of the building: ')
    replace(replacement_cost)
def replace(replacement_cost):
    # Find what 80% of the value is.
    insurance_value = replacement_cost * 0.8
    # State what the minimum insurance needed is.
    print 'The minimum amount of insurance you need is $%.2f' % insurance_value, ' dollars.'
main()
