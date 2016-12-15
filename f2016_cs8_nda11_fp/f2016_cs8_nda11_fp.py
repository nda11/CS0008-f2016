##name : Nabil Alhassani
# email : nda11@pitt.edu
# date :septemper/7th
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# Description: Final project
#
# Description:
# A customer needs to process a number of text files (called data files) that contain names and distance run by study participants.
# The format of those files is as follows:
#
# Max ,34.23
# Barbara ,23.00
# Luka ,12.87
# …
#
# In those files, each row is a comma separated list of 2 values: the first one is the name of the participant and the
# second is the distance that the participant has run.
# The names of the input files are stored one per line in an additional file, called the master input list.
# This file has the following structure:
#
# <data file 1>
# <data file 2>
# <data file 3>
# …

#
# Write a program that read the master input list file, retrieves the names of the data files and from each one of them
# reads every line, extract name and distance. Once the program has all the data in memory, it has to compute the following
# quantities and informations:
# - number of files read in input
# - total number of lines read
# - total distance run (aka the sum of all the distances loaded from provided files)
# - total distance run for each individual participant
# - individual maximum distance run and by which participant
# - individual minimum distance run and by which participant
# - report if there are any participants that appears more than once, how many times and their names
# - total number of participants
#
# The program should provide an terminal output similar to the following:
#
#	Number of Input files read   : xx
#	Total number of lines read   : xx
#
#	total distance run           : xxxx.xxxxx
#
#	max distance run             : xxxx.xxxxx
#	  by participant             : participant name
#
#	min distance run             : xxxx.xxxxx
#	  by participant             : participant name
#
#	Total number of participants : xx
#	Number of participants
#    with multiple records       : xx
#
# Name : xxxxxxxxxxxxxxxxxxx. Distance run : yyyy.yyyy. Runs : zzzz
#
# The program should also create an output file reporting name of the participant, how many times their name appears in
# the input files and the total distance run. Each row should be as follows:
#
# Max,3,124.23
# Barbara,2,65.00
# Luka,1,12.87
# …
#

#
# function getDataFromFile(file)
# read all the lines from the file, remove first line (header) and split all the others in name and distance
# insert a dictionary with name and distance in output list
#
# Input:
#  - file: (string) data file name
#
# Output
#  - data: (list) list of dictionaries, with each dictionary defined as follow:
#          { 'name': <participant_name>, 'distance' : <distance_run> }
#  - nlines: (integer) number of lines read from the file
def getDataFromFile(file):
    # initialize output list
    output = []
    # initialize line count
    nlines = 0
    # read file line by line
    for line in open(file, 'r'):
        # update number of lines read
        # exclude first line that is the header
        # we can recongize it because it contains the word "distance"
        if "distance" in line:
            # skip line
            continue
        # remove \n ending the line and split line at ","
        temp1 = line.rstrip('\n').split(',')
        # use try/except to avoid unhendled errors
        try:
            # append record to output list in the form of a dictionary with 2 keys: name and distance
            # remove unwanted spaces from name and convert distance to float
            output.append({'name': temp1[0].strip(' '), 'distance': float(temp1[1])})
            nlines += 1
        except:
            # here we catch all the lines that are incorrectly formatted
            # and we skipp them too
            print('Invalid row : ' + line.rstrip('\n'))
            # end try/except
    # end for
    # return data records
    return output, nlines


# end def getDataFromFile

#
# ask for master file from user
masterFile = input("Please provide master file : ")

# read master file and extract data files
try:
    dataFiles = [file.rstrip('\n') for file in open(masterFile, 'r')]
except:
    print("Impossible to read master file or invalid file name")
    exit(1)
# end try/except

# read data from data files
# we assume that the data files are accessible locally or we have the full path
#
# rawData is a list of 3 list which contains dictionaries with data from each file
rawData = [getDataFromFile(file) for file in dataFiles]

# number of files read
# this is equivalent to the number of elements in rawData
numberFiles = len(rawData)

#
# total number of lines read
# this is equivalent to the sum of the second item in each item of rawData
totalLines = sum([item[1] for item in rawData])

#

# ###put participant in class
#
class Participant:
    # class constructor
    def __init__(self, n, d=0):
        self.name = n
        self.distance = d
        # 1 if d != 0 else 0
        self.runs = int(d > 0)

    # increment total distance and runs counter
    def addDistance(self, d):
        self.distance += d
        self.runs += 1

    # sum up all distances in the list
    def addDistances(self, ld):
        self.distance += sum(ld)
        self.runs += len(ld)

    def getDistance(self):
        return self.distance

    def getName(self):
        return self.name

    def getRuns(self):
        return self.runs

    # string representation
    def __str__(self):
        return "Name : {0:20s}. Distance run : {1:9.4f}. Runs : {2:4d}".format(self.name, self.distance, self.runs)



##### it will be used instead of uniqueListData and participantDistances
participants = []
for data in rawData:
    for item in data[0]:
        # look up current data entry in participants list
        for i in range(len(participants)):
            if participants[i].getName()==item['name']:
                participants[i].addDistance(item['distance'])
                break
        else:  # if no participant with data['name'] found
            participant = Participant(item['name'], item['distance'])
            participants.append(participant)



# total number distance run by every participant
####this is equivalent of the sum of the "participant distance" element of the items in the participants
totalDistanceRun = sum([participant.getDistance() for item in participants])




# minum distance run with name
minDistance = {'name': None, 'distance': None}
# maximum distance run with name
maxDistance = {'name': None, 'distance': None}
# appearences dictionary
appearences = {}
#
# computes the total distance run for each participant iterating on all the participants
for p in participants:

    # if this is the first iteration or if the current participant distance is lower than the current min
    if minDistance['name'] is None or minDistance['distance'] > p.getDistance():
        minDistance['name'] = p.getName()
        minDistance['distance'] = p.getDistance()
    # end if
    # check if we need to update max
    # if this is the first iteration or if the current participant distance is lower than the current min
    if maxDistance['name'] is None or maxDistance['distance'] < p.getDistance():
        maxDistance['name'] = p.getName()
        maxDistance['distance'] = p.getDistance()
        # end if
# end for

#
# compute total number of participant
# this is equivalent to the length of the participants list
totalNumberOfParticipant = len(participants)
#
# #### compute total number of participants with more than one record
totalNumberOfParticipantWithMultipleRecords = 0
for p in participants:
    # has multiple runs
    if p.getRuns() > 1:
        # add number of participants with this number of records
        totalNumberOfParticipantWithMultipleRecords += 1
# end for




#
# set format strings
INTEGER = '5d'
FLOAT = '12.5f'
STRING = '20s'
#
# provide requested output
print("")
print(" Number of Input files read   : " + format(numberFiles, INTEGER))
print(" Total number of lines read   : " + format(totalLines, INTEGER))
print("")
print(" Total distance run           : " + format(totalDistanceRun, FLOAT))
print("")
print(" Max distance run             : " + format(maxDistance['distance'], FLOAT))
print("   by participant             : " + format(maxDistance['name'], STRING))
print("")
print(" Min distance run             : " + format(minDistance['distance'], FLOAT))
print("   by participant             : " + format(minDistance['name'], STRING))
print("")
print(" Total number of participants : " + format(totalNumberOfParticipant, INTEGER))
print(" Number of participants")
print("  with multiple records       : " + format(totalNumberOfParticipantWithMultipleRecords, INTEGER))
print("")
# loop to print all participant.
for p in participants:
    print(p)


#
# create output file
outputFile = "f2016_cs8_nda11_fp.output.csv"
# open file for writing
fh = open(outputFile, 'w')
# write header in file
fh.write('name,records,distance\n')
# loop on all the participants
for p in participants:
    # write line in file
    fh.write(','.join([p.getName(), str(p.getRuns()), str(p.getDistance())]) + '\n')
# end for
# close files
fh.close()