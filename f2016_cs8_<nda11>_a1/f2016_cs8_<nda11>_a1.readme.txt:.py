#name : Nabil Alhassani
# email : nda11@pitt.edu
# date :septemper/11th
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# Description:Starting with Python, Chapter 2,
# Notes:

#  first of all, I used follow chart to solve the problem . Next, start write down the steps :
# first, I  assign value to variables  USC and metric,also, I assign value to variables
# (1mile,1gallon,1liter, 1 kilometer. Then, I put an input that get user unit whether
#  USC number 1 #or Metric number 2.

# I started if and else condition using Boolean signs,
# choose between the two unit and Display #statement when user don't choose a unit.
# Then I put if, elif condition in side the if ,which start #with USC and Metric :

# in USC I:
# display the unit choose
# get distance drove by miles
# get consumption by gallon
# calculate the miles per gallon
# convert distance from mile to kilometer
# convert consumption from gallon to liters
# calculate the consumption from liters per kilometer

# Display the schedule

# set the consumption rate by using if and elif condition using boolean sign
# display the consumption rate after the schedule

# metric
# display the unit choose
# get distance drove by kilometers
# get consumption by liters
# convert distance from kilometer to mile
# convert consumption from liter to gallon
# calculate the miles per gallon
# calculate the consumption from liters per kilometer

# Display the schedule

# set the consumption rate by using if and elif condition using boolean sign
#and display
# the consumption rate after the schedule
#value to variables  USC and metric
USC=1
Metric=2
# assingn value to variables (1mile,1gallon,1liter, 1 kilometer )
one_mile=1.60934
one_gallon=3.78541
one_KM=0.621371
one_liter=0.264172

# get user unit input
input_1=input("what system you choose USC press number 1 or metric press 2:")

#condition chooes between two unit:
if input_1 ==1 or input_1 ==2:
    if input_1==1 :
        #USC
        # dispaly the unit chooes
        # get distance drove by miles
        # get consumption by gallon
        # calcualte the miles per gallon
        # convert distance from mile to kilometer
        # convert consumpsion from gallon to liters
        # calculate the consumption from liters per kilometer
        print('you choose USC measuerment')
        input_2=input('how many miles you drove:')
        input_3=input('how many number of gallons you used:')
        MPG = float(input_2 / input_3)
        km_drove= input_2*one_mile
        liter_used= input_3*one_gallon
        L_P_100K=float(100*liter_used/km_drove)


        # Dipaly the schedual
        print format('                             USC  \t  metric ')
        print format('Distance ______________:\t'),input_2,'miles\t'  ,km_drove,'km'
        print format('Gas ___________________:\t'),input_3,'Gallons\t',liter_used,'Liters'
        print format('Consumption ___________:\t'),MPG,'MPG\t',   L_P_100K,'l/100Km'


            # set the consumpiton rate by using if and elif condition and display
        # the consumption rate after the schedual

        if L_P_100K > 20:
            print('Gas Consumption Rating \t: Extremely poor')
        elif L_P_100K>15 and L_P_100K<= 20:
            print('Gas Consumption Rating \t: poor')
        elif L_P_100K>10 and L_P_100K<= 15:
            print('Gas Consumption Rating \t: Average')
        elif L_P_100K > 8 and L_P_100K <= 10:
            print('Gas Consumption Rating \t: Good')
        elif L_P_100K <= 8:
            print('Gas Consumption Rating \t: Exellent')









    elif input_1==2 :
        #metric
        # dispaly the unit chooes
        # get distance drove by kilometers
        # get consumption by liters
        # convert distance from kilometer to mile
        # convert consumpsion from liter to gallon
        # calcualte the miles per gallon
        # calculate the consumption from liters per kilometer
        print('you choose metric measuerment')
        input_4= input('how many number of kilometers you drove:')
        input_5= input('how many number of liters you used:')
        mile_drove=one_KM* input_4
        gallon_used=input_5/one_gallon
        MPG1=float(mile_drove/gallon_used)
        L_P_100K = float(100 * input_5 / input_4)

        # Dispaly the schedual

        print format('                             USC  \t    metric ')
        print format('Distance ______________:\t'),  mile_drove,'miles\t',     input_4,'km'
        print format('Gas ___________________:\t'), gallon_used,'Gallons\t',   input_5,'Liters'
        print format('Consumption ___________:\t'), MPG1, 'MPG\t',             L_P_100K,'l/100Km'



        # set the consumpiton rate by using if and elif condition and display
        # the consumption rate after the schedual
        if L_P_100K > 20:
            print('Gas Consumption Rating :    Extremely poor')
        elif L_P_100K > 15 and L_P_100K <= 20:
            print ('Gas Consumption Rating:    poor')
        elif L_P_100K > 10 and L_P_100K <= 15:
            print ('Gas Consumption Rating:    Average')
        elif L_P_100K > 8 and L_P_100K <= 10:
            print ('Gas Consumption Rating:    Good')
        elif L_P_100K <= 8:
            print ('Gas Consumption Rating:    Exellent')

# Dispaly when user don't choose a unit
else:
    print('choose measurment unite plz')



