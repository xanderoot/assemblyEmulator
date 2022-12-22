'''

this file handles the data as a string, passing data into these defs requires that it be converted into a string. [0,0,0,0,0,0,0,0] must be turned into '00000000'

this is for ease of use in the lookup table for ascii. data elsewhere should stay as lists for ease of data manipulation.

'''

################ imports

import time
from commonDefs import clear


lookupTable = {}
clockSpeed = 0.0

################ creates lookup table from text file

with open('ascii.txt') as txt:
    lookup = txt.readlines()

lookup = [each[:-1] for each in lookup] #remove \n from each string

for each in lookup:
    splitString = each.split('remove')
    lookupTable[splitString[2]] = splitString[1]

################ defs

def createDisplayRam(numberOfBytes=80,blank='00100000'):
    defaultData = []
    tempLookupTable = {}
    for x in range(numberOfBytes):
        tempLookupTable[hex(x)] = blank
    return tempLookupTable

displayRam = createDisplayRam()

def sendDisplayData(bus): # expects 16 bits in. first 8 instructions. last 8 data
    '''
    
    '''
    
    instruction = bus[0:8]
    data = bus[8:]
    

def printer():
    while True:
        lineOne = ''
        lineTwo = ''
        for x in range(len(displayRam)):
            if x < 40:
                temp = displayRam[hex(x)]
                lineOne += lookupTable[temp]
            else:
                temp = displayRam[hex(x)]
                lineTwo += lookupTable[temp]
        clear()
        print(lineOne)
        print(lineTwo)
        time.sleep(clockSpeed)

