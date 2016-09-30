# assingn value to variables  USC and metric
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
        print ('{}\t{0}\t {1} ').format('USC' 'Metric')
        print ('Distance ______________:\t{0:6.3f} Miles\t {1:6.3f}Km'.format(input_2,km_drove))
        print ('Gas ___________________:\t{0:6.3f} Gallons\t{1:6.3f}liter'.format(input_3,liter_used ))
        print ('Consumption ___________:\t{0:6.3f} MPG\t{1:6.3f}l/100Km'.format(MPG,  L_P_100K))




            # set the consumpiton rate by using if and elif condition and display
        # the consumption rate after the schedual

        if L_P_100K > 20:
            print('Gas Consumption Rating \t:  Extremely poor')
        elif L_P_100K>15 and L_P_100K<= 20:
            print ('Gas Consumption Rating \t: poor')
        elif L_P_100K>10 and L_P_100K<= 15:
            print ('Gas Consumption Rating \t: Average')
        elif L_P_100K > 8 and L_P_100K <= 10:
          print ('Gas Consumption Rating \t:   Good')
        elif L_P_100K <= 8:

          print ('Gas Consumption Rating \t: Exellent')









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
        print ('{}\t{0}\t {1} ').format('USC' 'Metric')
        print ('Distance ______________:\t{0:6.3f} Miles\t{1:6.3f}Km'.format(mile_drove, input_4))
        print ('Gas ___________________:\t{0:6.3f} Gallons\t{1:6.3f}liters'.format(gallon_used,input_5))
        print ('Consumption ___________:\t{0:6.3f} MPG\t {1:6.3f}l/100Km'.format(MPG1, L_P_100K))



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



