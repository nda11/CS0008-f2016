
# name : Nabil Alhassani
# email : nda11@pitt.edu
# date :septemper/11th
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# Description:Starting with Python, Chapter 2,
# Notes:
# any notes to the instructor and/or TA goes here
# ...and now let's program with Python

# exercise 6

# this program will convert fat and carbs to caluries
def main():

#Get fat and carbs have been eaten
    fat_gram=float(input("how many fat grams did you eat?"))
    carbs= float(input("how many carbs did you eat?"))
#assing function
    fat=cal_fat(fat_gram)
    carb1=cal_carbs(carbs)
#Dispaly the result
    print ('number of caluries result from fat',fat)
    print ('number of caluries result from carbs',carb1)
def cal_fat(fat_gram):
    fat=fat_gram*9
    return fat
def cal_carbs(carbs):
    carb1=carbs*4
    return carb1
main()