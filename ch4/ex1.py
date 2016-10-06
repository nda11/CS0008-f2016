
# name : Nabil Alhassani
# email : nda11@pitt.edu
# date :septemper/11th
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# Description:Starting with Python, Chapter 2,
# Notes:
# any notes to the instructor and/or TA goes here
# ...and now let's program with Python

# exercise 1
#Write a program in Python that keeps a running total of the number of bugs collected
#  during the seven days.
# The program should ask for the number of bugs collected each day,
# and when the loop is finished,
# the program should display the total number of bugs collected in the week.
# assign value to variable
# Initialize an accumulator variable.

bugs_collected = 0.0

# Ask the user to enter the number of bugs collected for each
# of the 5 days.
for counter in range(5):
    daily = input('Enter the number of bugs collected daily: ')
    bugs_collected = bugs_collected + daily

# Display the total bugs collected.
print 'The total number of bugs collected over 5 days was', bugs_collected
