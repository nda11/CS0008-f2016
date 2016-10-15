
# name : Nabil Alhassani
# email : nda11@pitt.edu
# date :septemper/11th
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# Description:Starting with Python, Chapter 2,
# Notes:
# any notes to the instructor and/or TA goes here
# ...and now let's program with Python

# exercise 5

def main():
    # input the user value_of_the_property
    value_of_the_property = input("Enter actual value of the property:")
    assessment = assessment_value(value_of_the_property)
    # displays the assessment_value and  property_tax
    print("Assessment value of the property is %.2f$."%assessment)
    print("Property tax is %.2f$."%property_tax(assessment))

def assessment_value(value_of_the_property):
    #calculate the assessment_value
    assessment = value_of_the_property*0.6
    return assessment

def property_tax(assessment):
    # Calculate the  property_tax
    tax = (assessment/100.00)*0.72
    return tax

main()