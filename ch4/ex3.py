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

#write a program that asks the user to enter the amount that
# he or she has budgeted (ie has to spend) for a month.
#Then, use a loop to prompt the user to enter his or her expenses for the month,
#  and keep a running total. When the loop finishes, the program should display:
#-amount budgeted
#-the total of the entered expenses
#- and the amount the user is under or over budget.

def budget_calculas():
    total_expanses=0
    monthly_budget=input('enter your budget for this month:')
    for i in range(30):
        cmd=input('enter your expenses:')
        total_expanses+=cmd
        print ('total expanses:'+str(total_expanses))

        total=monthly_budget-total_expanses
        if total>0:
            print('budget surplus:'+str(total))

        else:
            print ('budget defict:'+str(total))

budget_calculas()
