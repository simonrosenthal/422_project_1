import csv
from random import seed, randint
import os
from gpx_route import *
"""
SOURCES: 
https://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times-in-python
"""
output = 'output/'
input = 'input/'

def writeCSV(currentRoute):
    #thisRoute = Route()
    #thisRoute.turns = currentRoute.turns
    name = output + 'route' + str(randint(0,9999)) + '.csv'
    with open(name, 'w', newline='') as csvfile:
        fieldnames = ['Type', 'Notes', 'Distance']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        i = 0
        while (i < currentRoute.turnCount):
            writer.writerow({'Type': currentRoute.turns[i].direction, \
                             'Notes': currentRoute.turns[i].get_turnName(), \
                             'Distance': str(currentRoute.turns[i].get_distance())} \
                            )
            i+=1

def getNewestInput():
    newestFile = None
    for file in os.listdir(input):
        if(newestFile == None):
            newestFile = file
        if(os.path.getmtime( input + newestFile) < os.path.getmtime( input + file)):
            newestFile = file
    #print("newest inputted file is: " + str(newestFile))
    return input + str(newestFile)

def getNewestOuput():
    newestFile = None
    for file in os.listdir(output):
        if(newestFile == None):
            newestFile = file
        if(os.path.getmtime( output + newestFile) < os.path.getmtime( output + file)):
            newestFile = file
    #print("newest outputed file is: " + newestFile)
    return output + str(newestFile)