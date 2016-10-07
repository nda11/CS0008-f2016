def main():
    # Ask the user for their budget for the month.
    budget = input('What is your budget for the month? ')

    # Create a variable to control the loop.
    keep_going = 'y'

    # Calculate a series of expenses.
    while keep_going == 'y':
        # Ask the user to enter an expense.
        expense = input('Enter an expense: ')

        # Calculate the remainder of the budget.
        budget = budget - expense

        # State what the remaining budget is.
        print 'Your remaining budget is $%.2f.' % budget

        # Ask the user if they'd like to enter another expense.
        keep_going = raw_input('Do you want to calculate another ' + \
                               'expense (Enter y for yes): ')


# Call the main function.
main()
