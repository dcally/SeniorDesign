import numpy as np
import matplotlib.pyplot as plt
import random


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


def MainLoop():
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

