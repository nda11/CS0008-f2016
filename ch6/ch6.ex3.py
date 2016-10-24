# name : Nabil Alhassani
# email : nda11@pitt.edu
# date :septemper/11th
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# Description:Starting with Python, Chapter 2,
# Notes:
# any notes to the instructor and/or TA goes here
# ...and now let's program with Python

# exercise 3

# main function
def main():
    # progarm message
    print ('Line Numbers')

    #Ask user to enter file name
    file_name=input('Plz enter the file name:')
    # open file name
    infile=open(file_name,'r')
    infile.close()
    #initialize counter
    count=0

    #for loop
    for line in infile:
        count+=1
        #Display line
        print (count,":",line.rstrip("\n"))
        #close the file

    input()
main()