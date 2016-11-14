
# Template for code submission
# name : Nabil Alhassani
# email : nda11@pitt.edu
# date :septemper/7th
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# Description:Starting with Python, Chapter 2,
# Notes:
# 
# ...and now let's program with Python
# This program calculates how many lines and sum the distance run for
#two files and display the total.
# Assignment#2

# create a  processfile(fh)function

def processfile(fh):

# open file
    fo=open(fh,'r')
# assign variables to distance run and number of lines(ptn)
    pd =0
    ptn=0
# use for loop to read throw the file
    for line in fo:
#Remove the new line
        line=line.rstrip('\n')
#split the line
        temp=line.split(",")

# increase the counting distane run and number of lines
        pd+=1
        ptn+=float(temp[1])
#closing file.
        fo.close()
# return the distance and number of lines the function
        return ptn,pd

# create printKV function
def printKV(key,value, klen=0):

# Defining the key length and get the max space

    kl=max(len(key),klen)

    if(kl<klen):
        space=kl
        print(space)
# check if valu is intger and float using (isinstanc)
    if (isinstance(value,int)):
        print(format("%20s : %10d"%(key,value)))
    elif(isinstance(value,float)):
        print(format("%20s : %10.3f"%(key,value)))
    else:
        print(format(key,str(kl)+'s'))

# The infinite loop ask the user for file name

while (True):
    #prompt the user to enter file name
    fo = input(("File read:"))
    try:
        print ('')
        if fo == "quite" or fo == "q":
                print ('')
# display the exit statment
                print('File to be read: Quit ')
                exit()

#the file go back to be processe(fh) function
        pd,ptn=processfile(fo)
# display the Total# of lines and distance run

        printKV("Partial Total# of lines", ptn,)
        printKV("Partial Total distance run", pd)
        print("")
# close the file

#Assing value to Total# of lines and "Total distance run
        ttn=0
        ttd=0
#calculat and itirate the total # of lines and total distance run
        ttn+=ptn
        ttd+=pd
# dispaly the total # of lines and total distance run

        print('Totals')
        printKV('Total# of lines',ttn,)
        printKV("Total distance run", ttd)
        print('')
# the excpttion possible IOError and NameError
    except IOError :
        print ('Not found the file')
    except NameError:
        print ('File is not defined')

