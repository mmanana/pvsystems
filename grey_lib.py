# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 14:58:04 2016

@author: Ryan
"""

#Change Directory to make sure all files are in the same folder

import numpy as np
import matplotlib.pyplot as plt
import csv as csv
import pandas as pd
import math as math


def plotHistogram(csv1): #imput the csv data file
    weather = pd.read_csv("measurements_file.txt.txt", sep=';',header=0,encoding='utf-16')
    sr=weather['solarRadiation']
    nbins=100
    hist, bins, patches =plt.hist(sr,nbins)

    plt.xlabel('Solar Radiation [W/m^2]')
    plt.ylabel('Frequency')
    plt.title('Solar Radiation Histogram')
    plt.show()

    return
    
def plotpdf(csv1): #imput the csv data file
     weather = pd.read_csv("measurements_file.txt.txt", sep=';',header=0,encoding='utf-16')
     sr=weather['solarRadiation']
     nbins=100
     hist, bins, patches =plt.hist(sr,nbins,normed=1)
     
     
     plt.xlabel('Solar Radiation [W/m^2]')
     plt.ylabel('Realtive Frequency')
     plt.title('Solar Radiation PDF')
     plt.show()
     
     return
     
     #Beta=OptimumSlope sys_losses=60%, PanelArea=0.1015*0.1015 timespan=300seconds
def calc_energysupplied(sr,beta,sys_losses,PanelArea,timespan):
    weather = pd.read_csv("measurements_file.txt.txt", sep=';',header=0,encoding='utf-16')
    sr=weather['solarRadiation']     
    energy=math.cos(math.radians(beta))*sr*sys_losses*PanelArea*timespan
    EnergySupplied=sum(energy)
    print EnergySupplied
    
    return 
    



def plotWindhistogram(csv1):
    weather = pd.read_csv("measurements_file.txt.txt", sep=';',header=0,encoding='utf-16')
    windSpeed=weather['windSpeed']
    nbins=50
    hist, bins, patches=plt.hist(windSpeed,nbins)
    
    plt.xlabel('Wind Speed [m/s]')
    plt.ylabel('Frequency')
    plt.title('Wind Speed Histogram')
    plt.show()

    return
#depending on the value of the windspeed, the energy supplied by the turbine follows a piecewise function.
def calc_windenergy(csv1): #imput the csv datafile
    weather = pd.read_csv("measurements_file.txt.txt", sep=';',header=0,encoding='utf-16')
    windSpeed=weather['windSpeed']
    for element in windSpeed:
        if element in xrange(0,3):
            windenergy=0
        elif element in xrange(3,10):
            windenergy=(257.143*(windSpeed-3))*0.08333  #5 minutes=0.08333 hr
        elif element in xrange(10,25):
            windenergy=154.1667 #1850kW*0.0833 hr
        else:
            windenergy=0
        totalwindenergy=sum(windenergy)
        print totalwindenergy
        return
       
       

print "This is the solution of problem 1.1.1"
print "Optimum slope determined by the PV-gis system is 35 degrees"   
    
print "This is the solution of problem 1.1.2"    
csv1="\\measurements_file.txt.txt"
plotHistogram(csv1)

print "This is the solution of problem 1.1.3"
plotpdf(csv1)

print "This is the solution of problem 1.1.4"
print "Energy Supplied by the system(W*hr):"
calc_energysupplied(csv1,35.0,0.6,0.0103,300)

print "This is the solution of the problem 1.2.1"
plotWindhistogram(csv1)

print "This is the solution of the problem 1.2.2"
print "Energy supplied by the Wind turbine (kW*hr):"
calc_windenergy(csv1)


