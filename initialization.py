################

def createRegisters(accumulator=1,indexReg=2,StatusFlags=1,bits=8,blank=0):
    returnData = {}
    defaultData = []
    for x in range(bits):
        defaultData.append(blank)
    for x in range(accumulator):
        returnData['accumulator{}'.format(x)] = defaultData
    for x in range(indexReg):
        returnData['indexRegister{}'.format(x)] = defaultData
    for x in range(StatusFlags):
        returnData['statusFlags{}'.format(x)] = defaultData
    return returnData


################

def createEmptyEEPROM(RegisterSize=16,bits=8,blank=0):
    tempEEPROM = {}
    defaultData = []
    for x in range(bits):
        defaultData.append(blank)
    memSize = bits
    for x in range(16):
        memSize *= 2    
    for x in range(int(memSize)):
        tempEEPROM[hex(x)] = defaultData
    return tempEEPROM

################

def createEmptyRam(registerSize=16,bits=8,blank=0):
    tempRam = {}
    defaultData = []
    for x in range(bits):
        defaultData.append(blank)
    memSize = bits
    for x in range(registerSize):
        memSize *= 2    
    for x in range(int(memSize)):
        tempRam[hex(x)] = defaultData
    return tempRam

################

def createAddressBus(numberOfBusses=1,bits=16,blank=0):
    defaultData = []
    addressBus = {}
    for x in range(bits):
        defaultData.append(blank)
    for x in range(numberOfBusses):
        addressBus['addressBus{}'.format(x)] = defaultData
    return addressBus


################

def createDataBus(numberOfBusses=1,bits=8,blank=0):
    defaultData = []
    dataBus = {}
    for x in range(bits):
        defaultData.append(blank)
    for x in range(numberOfBusses):
        dataBus['dataBus{}'.format(x)] = defaultData
    return dataBus