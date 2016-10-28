# name : Nabil Alhassani
# email : nda11@pitt.edu
# date :septemper/11th
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# Description:Starting with Python, Chapter 2,
# Notes:
# any notes to the instructor and/or TA goes here
# ...and now let's program with Python

# exercise 2

def main():
    # ask user the file name
    file1=open(input(str('Plz what is the file you want to open')),'r')
    #read fist line from the txt file
    line=file1.readline()
    count=0
    # use while loop to continue iteration till five
    while line!=''and count<5:

        #display line
        print (line)

        # read  line from the txt file
        line = file1.readline()
        count+=1

        #close the file
    file1.close()
# call the main function
main()

#


