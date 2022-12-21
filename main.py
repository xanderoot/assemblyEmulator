################ imports and declarations

import initialization as init

################ todo add loop to get user preferences for hardware initialization

################ 'hardware' setup loop

# defaults to 6502 hardware
registers = init.createRegisters()
ram = init.createEmptyRam()
storage = init.createEmptyEEPROM()
addressBus = init.createAddressBus()
dataBus = init.createDataBus()
print(registers,'\n',addressBus,'\n',dataBus)


################ eeprom programmer



################ processing loop