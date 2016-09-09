

# Exercise : ch2-ex3
#This program asks the user to enter the total square meters of land and calculates the number of
#acres in the tract.
#set one_acre value and
one_acre= 4,046.8564224**2
one_square_meter= 0.000247105
#input square_meter
square_meter=float(input('enter the total square meters:',))
# calculation the acre in the tract.
acre=square_meter * one_square_meter
# Display the total acre
print("this is the total acre:",acre)

