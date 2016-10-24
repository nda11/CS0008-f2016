# name : Nabil Alhassani
# email : nda11@pitt.edu
# date :septemper/11th
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# Description:Starting with Python, Chapter 2,
# Notes:
# any notes to the instructor and/or TA goes here
# ...and now let's program with Python

# exercise 4

# main function
def main():
    # progarm message
    print ('item counter')

    # open file name
    infile=open('names.txt','r')
    #initialize counter
    count=0

    #for loop
    for line in infile:
        count+=1
        #Display line
        print (line.rstrip("\n"))
        print ('total name:',count)
        #close the file
    infile.close()
    input()
main()