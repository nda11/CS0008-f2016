# name : Nabil Alhassani
# email : nda11@pitt.edu
# date :septemper/11th
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# Description:Starting with Python, Chapter 2,
# Notes:
# any notes to the instructor and/or TA goes here
# ...and now let's program with Python

# exercise 4


def main():

# ask user to enter monthly cost for six expenses
    inp1=float(input('the expense of loan payment per month $:'))
    inp2=float(input('the expense of insurance  per month $:'))
    inp3=float(input('the expense  of gas  per month $:'))
    inp4=float(input('the expense  of oil per month $:'))
    inp5=float(input('the expense  of tires per month $:'))
    inp6=float(input('the expense  of maintenance per month $:'))
    total_expences_per_month(inp1 ,inp2 , inp3 , inp4 , inp5 , inp6)


def total_expences_per_month(inp1 ,inp2 , inp3 , inp4 , inp5 , inp6):
    # calculate and print monthly cost.
    total_expences_per_month=inp1+ inp2+ inp3+ inp4+ inp5+ inp6
    print('This is the monthly cost: $', format(total_expences_per_month, ',.2f'))

    total_expences_per_year( total_expences_per_month)

def total_expences_per_year(total_expences_per_month):
    # calculate and print year cost
    total_expences_per_year=total_expences_per_month * 12
    print('This is the yearly cost: $', format(total_expences_per_year, ',.2f'))

main()