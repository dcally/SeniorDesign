import numpy as np
import matplotlib.pyplot as plt
import random
import spidev
import time
import RPi.GPIO as GPIO
from guizero import App

finalFreq = 500000
StartcurFreq = 200000

def initialize():
    print("Initialization")
    TransmitBits()
    RecieveBits()
    DisplayGraph()
    MainLoop()
    print("Program Closed")

def TransmitBits():
    print("Transmit Bits")
    ResonantFrequency(StartcurFreq)
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
    #curFreq is the Current Frequnecy being measured in Hz (ie 200000 is 200kHz)

    #TODO: ASK WHERE THIS VALUE IS COMING FROM
    inputBits = [0b0000000000000000000000000000000000000000]
    # finalFreq is the last frequnecy in the sweep, in this it should be 500kHz
    if(curFreq < finalFreq):
        # Start SPI
        spi = spidev.SpiDev(0, 1)  # create spi object connecting to /dev/spidev0.1
        spi.max_speed_hz = curFreq  # start set speed to current frequency in Hz

        # Set FQUID to 1
        GPIO.output(17, 1)
        time.sleep(0.1)
        # Set FQUID to 0
        GPIO.output(17, 0)

        #SPI the 40 input bits
        spi.writebytes(inputBits)  # write 40 bits
        time.sleep(0.01)  # sleep for 0.01 seconds

        # Required FQUID Pulse
        GPIO.output(17, 1)
        time.sleep(0.1)
        GPIO.output(17, 0)

        spi.close()  # always close the port before exit

        curFreq = curFreq + 1000
        ResonantFrequency(curFreq)
    else:
        return

def adcValues():
    #Pulse SCK

    #Wait 10 miliseconds
    time.sleep(0.01)

    #turn CONV High

    #Wait 1 miliseconds
    time.sleep(0.001)

    #Set SClk slower than 90 Mhz

    #Recieved Bits

    #Sleep/Nap Mode

    return

def MainLoop():
    #Set up pins for GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    #FQUD pin 17 for DDS, Pin 18m is the CONV pin for ADC
    pins = [4, 17, 18]
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

    #Start GUI
    app = App(title="Senior Design")
    StartTransmitBits = PushButton(app, command=ResonantFrequency(200000), text="Transmit Bits")
    app.display()



    # programRunning = True
    # takeMeasurements = True
    # transmitData = False
    # recieveData = False
    # closeProgram = False
    # #while programRunning:
    # while False:
    #     if(takeMeasurements):
    #         FindMeasurements()
    #         takeMeasurements = False
    #         transmitData = True
    #         recieveData = False
    #         closeProgram = False
    #     elif(transmitData):
    #         TransmitBits()
    #         takeMeasurements = False
    #         transmitData = False
    #         recieveData = True
    #         closeProgram = False
    #     elif(recieveData):
    #         RecieveBits()
    #         takeMeasurements = False
    #         transmitData = False
    #         recieveData = False
    #         closeProgram = True
    #     elif(closeProgram):
    #         programRunning = False
    #     #To Avoid Inifinite Loops
    #     else:
    #         programRunning = False

    return

