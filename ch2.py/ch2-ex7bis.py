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

# exercise 7
# This program ask user to enter number of miles driven and the gallons of gas used
# can be calculated with the following formula:
#L per 100Km = 100 * Liters used / Kilometers driven
#This program that ask the user for the number of miles
# driven and the gallons of gas used.
#It should convert to metrics and than display Km driven,
# liters used and L per 100Km.

#Answer
#input number of miles driven
Miles= input('how many the number of miles you have driven?:')

#input number of gallons of gas used.
gallons_gas=input('how many number of gallons of gas you used?:')

# assign Kilometers and liter_uesd
#  calculate miles_per_gallon, Km_per_Liter and L_per_100Km
#

Kilometers=1.6 * Miles
liter_uesd=3.78 * gallons_gas

miles_per_gallon = float (Miles) / float (gallons_gas)

Km_per_Liter= Kilometers / liter_uesd

L_per_100Km = 100 * liter_uesd / Kilometers

#Display the result:
#miles_per_gallon have driven
#Kilometers you have driven
#literhave used
#Km_per_Liter have driven
#L_per_100Km will consume

print ('you have driven',miles_per_gallon,'MPG on your trip')

print ('you have driven:',Kilometers,'km on your trip')

print ('you have used:',liter_uesd,'liter on your trip')

print ('you have driven',Km_per_Liter,'KPL on your trip.')

print ('you will consume',L_per_100Km,'L_per_100Km')
