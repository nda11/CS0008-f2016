## name : Nabil Alhassani
# email : nda11@pitt.edu
# date :septemper/11th
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# Description:Starting with Python, Chapter 2,
# Notes:
# any notes to the instructor and/or TA goes here
# ...and now let's program with Python

# exercise 15
# Write a program that asks the user to enter five test scores.
# The program should display a letter grade for each score and the average test score.
# Write the following functions in the program:

#calc_average - this function should accept five test scores as arguments and return
#  the average of the scores.

#determine_grade - this function should accept a test score as an argument
# and return a letter grade for the score, based on the following grading scale

#90 - 100 A

#80 - 89 B

#70 - 79 C

#60 - 69 D

#below 60 F


def main():
    #
    # Variable           Type                Purpose
    # testavg            int                 holds the test average all scored tests
    # grade              string              holds the letter grade for test
    #


    testavg = calc_average(validate)
    grade = determine_grade(testavg)

    print("The avergage Test score is ", testavg, "that makes it", grade)


def calc_average(validate):
    #
    # This function asks for accepts the test scores of 5 tests
    # Then it will calculate the average and return it to the main for later use
    #
    # Variable           Type            Purpose
    # test1              float           holds Test score for test 1
    # test2              float           holds Test score for test 2
    # test3              float           holds Test score for test 3
    # test4              float           holds test score for test 4
    # test5              float           holds test score for test 5
    # testavg            float           holds the average test score
    #

    test1 = float(input("Please enter the score for Test #1: "))
    test1 = validate(test1)
    test2 = float(input("Please enter the score for Test #2: "))
    test2 = validate(test2)
    test3 = float(input("Please enter the score for Test #3: "))
    test3 = validate(test3)
    test4 = float(input("Please enter the score for Test #4: "))
    test4 = validate(test4)
    test5 = float(input("Please enter the score for Test #5: "))
    test5 = validate(test5)


    grade = determine_grade(test1)
    print ("The Score for Test #1 is: ", test1, " which is a ", grade)
    print()



    grade = determine_grade(test2)
    print ("The Score for Test #2 is: ", test2, " which is a ", grade)
    print()



    grade = determine_grade(test3)
    print("The Score for Test #3 is: ", test3, " which is a ", grade)
    print()



    grade = determine_grade(test4)
    print("The Score for Test #4 is: ", test4, "which is a ", grade)
    print()



    grade = determine_grade(test5)
    print("The Score for Test #5 is: ", test5, "which is a ", grade)
    print()

    testavg = (test1 + test2 + test3 + test4 + test5) / float(5)

    return testavg


def validate(score):
    #
    # This function validates the test scores. It makes sure the test scores are
    # at least a 0 and no more than 100.
    #
    # Variable           Type            Purpose
    # score              float           holds the test score



    while score < 0 or score > 100:
        print ("The score must be at least 0 and no more then 100")
        score = float(input("Please Re-Enter Your Test Score: "))

    return score


def determine_grade(testavg):
    #
    # Thie function gives the test score its letter grade (GPA) for the test and returns it
    #
    # Variable       Type            Purpose
    # testavg
    grade='F'
    if testavg >= 90 and testavg <=100 :
        grade = 'A'
    elif testavg >= 80 and testavg <=89:
        grade = 'B'
    elif testavg >= 70 and testavg <=79:
        grade = 'C'
    elif testavg >= 60and testavg <=69:
        grade = 'D'


    return grade


main()