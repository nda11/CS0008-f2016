#This program gets the speed and hours driven of
#a vehicle then uses a loop and calculates the
#miles driven for each hour (3 hours)

#Get the speed of the vehicle in miles per hour
speed = int(input("What was the speed of the vehicle (MPH)?\n"))

#Get the number of hours driven
hours_driven = int(input("How many hours did you drive?\n"))

print("{:>5}{:>10}".format("Hour", "Distance"))

for hour in range(1, hours_driven+1):
	print("{:>1}{:>10}".format(hour, hour * speed))