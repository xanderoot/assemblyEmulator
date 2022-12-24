################ imports and declarations

from initialization import * # used to create the hardware
import display # only used to change values in display
from multiprocessing import Process# used to create displays and outputs
from commonDefs import *


display.clockSpeed = .1 # 10 Hz

################ todo add loop to get user preferences for hardware initialization

################ 'hardware' setup loop

# defaults to 6502 hardware
registers = createRegisters() # accumulator=1,indexReg=2,StatusFlags=1,bits=8,blank=0
ram = createEmptyRam() # registerSize=16,bits=8,blank=0
storage = createEmptyEEPROM() # RegisterSize=16,bits=8,blank=0
addressBus = createAddressBus() # numberOfBusses=1,bits=16,blank=0
dataBus = createDataBus() # numberOfBusses=1,bits=8,blank=0

# display setup loop

'''if __name__ == '__main__': # runs concurrently with program.
    displayLoop = Process(target=display.printer)
    displayLoop.start()'''

################ eeprom programmer




################ processing loop