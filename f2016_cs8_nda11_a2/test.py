
import os.path

# contants
# length of the key
FORMAT_KEY_LENGTH = 30

#
# printKV function
def printKV(key,value,klen = 0):
    # check which is the length to be used when printing the key
    # max of klen and the length of key
    klen = max(klen,len(key));
    # check which is type of value and choose the proper formatting
    if isinstance(value,str):
        # we have a string
        fvalue = '20s'
    elif isinstance(value,float):
        # we have a float
        fvalue = '10.3f'
    elif isinstance(value,int):
        # we have a integer
        fvalue = '10d'
    else:
        # we do not know what we have,
        # so we try our best to convert it to a string and
        # format it as a string
        value = str(value)
        fvalue = '20s'
    # end if
    #
    # print key and value with correct formatting
    print(format(key,'>'+str(klen)+'s'),' : ',format(value,fvalue))
# end def

# processFile function
def processFile(fh):
    # count how many lines the files has and sum the distance that is the second field of each line
    #
    # initialize partial accumulators
    # partial total distance
    ptd = 0
    # partial total number of lines
    ptn = 0

    # loops on all the lines in the files
    # we hope that the read position is at the beginning of the file
    for line in fh:
        # in each iteration, we got the next line from the file
        #
        # remove new line (/n) and split in two parts: name and number
        [name, distance] = line.rstrip('\n').split(',')
        # convert distance from string to float
        distance = float(distance)
        # print name and distance in this record properly formatted
        printKV('Name', name, FORMAT_KEY_LENGTH)
        printKV('Distance', distance, FORMAT_KEY_LENGTH)
        #
        # update partial accumulators
        # partial total distance
        ptd += distance
        # partial total number of lines
        ptn += 1
    # for
    #
    # returns partials
    return [ptn, ptd]
#end def

# initialize totals partials
# total distance
td = 0
# total number of lines
tn = 0
# number of files
nf = 0

#
#  ask the user for the first file
print('Please enter the name of the first file to process.')
file = input('File name : ')

# check if file name is empty, or is q or quit and also if
while ( file != '' and file != 'quit' and file != 'q' and os.path.exists(file) ):

    # open the file in read mode and creates the file object
    fh = open(file, 'r')
    # process the file and get the number of lines and the sum of the distances
    ptn, ptd = processFile(fh)
    # close the file
    fh.close()

    # update total accumulators
    # number of files
    nf += 1
    # total distance
    td += ptd
    # total number of lines
    tn += ptn

    # ask the user the next file
    print('Please enter the name of the next file to process. Leave empty or type q/quit to exit')
    file = input('File name : ')

#while

# print report
print('')
printKV('Files read', nf, FORMAT_KEY_LENGTH)
printKV('Total Distance', td, FORMAT_KEY_LENGTH)
printKV('Names found', tn, FORMAT_KEY_LENGTH)
print('')
