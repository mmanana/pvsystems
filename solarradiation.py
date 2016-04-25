# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 18:20:11 2016

File: solarradiation.py
Description: Compute solar radiation

Input:
n: Day of the year. Integer [1, 365]

Output:
Gon: Solar radiation density

@author: Mario
"""
import math

def Gon( n):
    GSC=1367.0 # W/m^2
    Gon=GSC*(1+0.033*math.cos(2.0*math.pi*n/365.0))
    return Gon

def SolarDistance():
    return 1.495e11


def EarthDiameter():
    return 1.27e7


def SunDiameter():
    return 1.39e9