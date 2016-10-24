# name : Nabil Alhassani
# email : nda11@pitt.edu
# date :septemper/11th
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# Description:Starting with Python, Chapter 2,
# Notes:
# any notes to the instructor and/or TA goes here
# ...and now let's program with Python

# exercise 1

def main():
    # open file
    outfile=open('number.txt','w')
    outfile.write('1\n 2\n 3\n')
    # close file
    outfile.close()

# create file variable and name it (file1) the file name is numbres.txt
# open it
# use read mode(e)
# Open the file
    file1=open('number.txt','r')

# use for loop to read all line from in file
    for line in file1:
        num=int(line)
        # display the numbers in the f1
        print (num)
    #close the file
    file1.close()

# Call the main function
main()

# the output:
# f1=open('number.txt','r')
#IOError: [Errno 2] No such file or directory: 'number.txt'