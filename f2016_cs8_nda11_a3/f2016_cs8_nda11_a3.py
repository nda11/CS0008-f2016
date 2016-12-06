#name : Nabil Alhassani
# email : nda11@pitt.edu
# date :septemper/7th
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# Description:Starting with Python, Chapter 2,
# Notes:
#
# ...and now let's program with Python

#This program that read the master input list file,
# retrieves the names of the data files and from each
#one of them reads every line, extract name and distance.
# Once the program has all the data in memory,
#it has to compute the following quantities and informations:
#• number of files read in input
#• total number of lines read
#• total distance run (aka the sum of all the distances loaded from provided files)
#• total distance run for each individual participant
#• individual maximum distance run and by which participant
#• individual minimum distance run and by which participant
#• report if there are any participants that appears more than once,
#how many times and their
#names
#• total number of participants
# Assignment#3


import os.path


# MN: what does this function do?
def read_txt(filename):
    fp = open(filename, 'r')
    # make a list of file lines
    lines = []
    for line in fp:
        lines.append( line.rstrip('\n') )
    fp.close()
    return lines


# MN: what does this function do?
def read_csv(filename):
    # list of lines
    lines = []
    # partial total distance
    ptd = 0
    # partial total number of lines
    ptn = 0
    fp = open(filename, 'r')
    # skip csv header
    header = fp.readline()
    for line in fp:
        # split line by comma
        name, dist = line.split(',')
        # strip training spaces from the name
        # and convert the distance to float
        lines.append([name.strip(), float(dist)])
        ptn = ptn + 1
        ptd = ptd + float(dist)
    fp.close()
    return (lines, ptn, ptd)




def main():
    # MN: I would specify that you are asking for the master list file
    print('Please enter the name of file')
    filename = input('enter the file name:')
    # Lower input
    # MN: this statement transform the string to all lower case but the result is lost
    #     because you are not assigning it to a variable
    #     Check: https://docs.python.org/3.5/library/stdtypes.html#str.lower
    #     it states that lower method returns a copy and does not change the original string
    filename.lower()
    # MN: why are you using a while loop on the filename
    #     we have only one master list file, so you read it once and you are done.
    # check if file name is empty, or is q or quit
    while (filename != '' and filename != 'quit' and filename != 'q' and os.path.exists(filename)):
        # to exit the progra
        # read a list of input csv files
        csv_files = read_txt(filename)

        tn = 0
        td = 0
        data = []
        # gather all (name, dist) from input files
        for fname in csv_files:
            pdata, ptn, ptd = read_csv(fname)
            tn = tn + ptn
            td = td + ptd
            for name, dist in pdata:
                data.append((name, dist))
                # set of distinct names
        # MN: describe what you have in data
        #
        # MN: I assume that in participant you have the full list of unique names, correct?
        participants = set()
        for name, dist in data:
            participants.add(name)

        # dict of name mapped to a list of distances
        records = {}
        for person in participants:
            items = []
            # gather distances run by person
            for name, dist in data:
                if name == person:
                    items.append(dist)
            records[person] = items

        # MN: this solution works, but you could combine computing min and max in one loop
        #     reducing by one loop
        # minimal individual distance
        min_dist_name, min_dist = data[0]
        for name, dist in data:
            if dist > min_dist:
                min_dist = dist
                min_dist_name = name

        # maximum individual distance
        max_dist_name, max_dist = data[0]
        for name, dist in data:
            if dist < max_dist:
                max_dist = dist
                max_dist_name = name

        # dict of records that have more than 1 entry
        multiple_records = {}
        for key, val in records.items():
            if len(val) > 1:
                multiple_records[key] = val
                # display the output

            # MN: why are you placing the printing here with this indentation?
            #     this would  get executed as many time as the for loop
            #     but you interrupt with the exit() 
            #     The correct solution would be to indent it so it is execute after the last loop
            
	print('Number of Input files read    : {0}'.format(len(csv_files)))
        print('Total number of lines read    : {0}'.format(tn))
        print('')
        print('total distance run            : {0:11.5f}'.format(td))
        print('')
        print('max distance run              : {0:2.3f}'.format(min_dist))
        print('  by participant              : {0}'.format(min_dist_name))
        print('')
        print('min distance run              : {0:2.3f}'.format(max_dist))
        print('  by participant              : {0}'.format(max_dist_name))
        print('')
        print('Total number of participants  : {0}'.format(len(participants)))
        print('Number of participants')
        print(' with multiple records        : {0}'.format(len(multiple_records)))
        print('')
        # MN: no exit is required
        #exit()

main()
