


# create a  processfile(fh)function

def processfile(fh):

# open file
    fo=open(fh,'r')
# assign variables to distance run and number of lines(ptn)
    pd =0
    ptn =0
# use for loop to read throw the file
    for line in fo:
#Remove the new line
        line=line.rstrip('\n')
#split the line
        temp=line.split(",")
#assing distance to value
        dist=float(temp[1])
# increase the counting distane run and number of lines
        ptn += 1
        pd+=dist
# return the distance and number of lines the function
        return ptn,pd

# create printKV function
def printKV(key,value, klen=0):
# Defining the key length and get the max space

    kl=max(len(key),klen)

    if(kl>klen):
        space=kl
        print(space)
# check if valu is intger and float using (isinstanc)
    if (isinstance(value,int)):
#print
        print("%20s : %10d"%(key,value))
    elif(isinstance(value,float)):
        print("%20s : %10.3f"%(key,value))
    else:
        print (format(key,str(kl)+'s'))
# The infinite loop ask the user for file name
while (True):
#use try to
    try:
        print ('')
# get the file name
        fh = input(("File read:"))
# if condition to exit the program
        if(fh=="quite"and fh=="q"):
            print ('')
            print('File to be read: Quit ')
            exit()
#the file go back to be processed
        pd,ptn=processfile(fh)
# display the Total# of lines and distance run
        printKV("Partial Total# of lines", ptn,)
        printKV("Partial Total distance run", pd)
        print("")
# close the file
        fh.close()
#Assing value to Total# of lines and "Total distance run

        ttn=0
        ttd=0
#calculat and itirate the total # of lines and total distance run
        ttn+=1+pd
        ttd+=1+ptn
# dispaly the total # of lines and total distance run
        print('')
        print('Totals')
        print('Total# of lines',ttn,)
        print("Total distance run", ttd)
        print('')
# the exxpttion possible IOError,NameError,SyntaxError and TypeError
    except IOError:
        print ('Not found the file')
    except NameError:
        print ('File is not defined')
    except SyntaxError:
        print ('invalid syntax')
    except TypeError:
        print ('coercing to Unicode: need string or buffer, type found')