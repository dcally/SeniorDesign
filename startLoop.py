import numpy as np
import matplotlib.pyplot as plt
import random
import spidev
import time

finalFreq = 500

def initialize():
    print("Initialization")
    TransmitBits()
    RecieveBits()
    DisplayGraph()
    MainLoop()
    print("Program Closed")

def TransmitBits():
    print("Transmit Bits")
    return

def RecieveBits():
    print("Recieve Bits")
    return

def DisplayGraph():
    print("Display GUI Graph")
    return

def FindMeasurements():
    print("Find Measurements")
    return

def ResonantFrequency(curFreq):
    #curFreq is the Current Frequnecy being measured in kHz (ie 200 is 200kHz)
    #finalFreq is the last frequnecy in the sweep, in this it should be 500kHz
    if(curFreq < finalFreq):
        #Set FQUID to 1

        #Set FQUID to 0

        #Send the first D7 bit
        BitSending(0)

        #Recursive Function
        curFreq = curFreq + 1
        ResonantFrequency(curFreq)
    else:
        return

def BitSending(curbit):
    if(curbit < 40):
        #Send Bit

        #Recursive Function
        curbit = curbit + 1
        BitSending(curbit)
    else:
        return

def MainLoop():
    spi = spidev.SpiDev()

    # Open a connection to a specific bus and device (chip select pin)
    spi.open(bus, device)

    # Set SPI speed and mode
    spi.max_speed_hz = 500000
    spi.mode = 0

    # Clear display
    msg = [0x76]
    spi.xfer2(msg)

    time.sleep(2000)


    programRunning = True
    takeMeasurements = True
    transmitData = False
    recieveData = False
    closeProgram = False
    while programRunning:
        if(takeMeasurements):
            FindMeasurements()
            takeMeasurements = False
            transmitData = True
            recieveData = False
            closeProgram = False
        elif(transmitData):
            TransmitBits()
            takeMeasurements = False
            transmitData = False
            recieveData = True
            closeProgram = False
        elif(recieveData):
            RecieveBits()
            takeMeasurements = False
            transmitData = False
            recieveData = False
            closeProgram = True
        elif(closeProgram):
            programRunning = False
        #To Avoid Inifinite Loops
        else:
            programRunning = False

    return

