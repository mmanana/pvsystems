# -*- coding: utf-8 -*-
"""
Created on Sun May 08 15:31:18 2016
Last update on Sun May 08

@author: Mario Mañana Canteli
@Department: Electrical and Energy Engineering
@Company: University of Cantabria. Spain
"""
import math


def Gon( day):
    # day .- Day of the year
    Gsc=1367.0  # Value adopted by Duffie-Beckman. Book SOLAR ENG. of 
                # THERMAL PROCESSES. pg. 10
    Gon=Gsc*(1.0+0.033*math.cos(360.0*day*math.pi/(365.0*180.0)))
    return Gon
    
    
def DayOfYear( day, month):
    # day .- Day of the month
    # month .- Month
	# return .- Day of year
    offset=[0,0,31,59,90,120,151,181,212,243,273,304,334]
    DoY=offset[month]+day
    return DoY
    

def Declination( day):
    # day .- Day of the year
    delta=23.45*math.sin( (284.0+day)*360.0*math.pi/(365.0*180.0))
    return delta
    

def LongStd( Long):
    # Longitud in degrees [0, 360º] East
    LongStd=15*math.ceil( Long/15.0)
    return LongStd
   
   
def ET( day):
    # day .- day of the year
    B=(day-1)*360.0/365.0
    B=B*math.pi/180.0
    a=0.001868*math.cos(B)
    b=0.032077*math.sin(B)
    c=0.014615*math.cos(2*B)
    d=0.04089*math.sin(2*B)
    ET=229.2*(0.000075+a-b-c-d)
    return ET
    
    
def HMtoStandardTime( day, month, hour, minute):
    # Standard time. Daylight Saving Time is taken into account
    # 
    DoY=DayOfYear( day, month)
    start=DayOfYear( 27, 3)
    end=DayOfYear( 30, 10)
    if (DoY>=start) and (DoY<end):
        if hour >= 1:
            hour=hour-1
        else:
            hour=23
            day=day-1
    StdTime=hour*60+minute
    return StdTime


def StandardTimetoSolarTime( day, month, hour, minute, Long):
    # day .- Day of the month
    # month .- Month of the year
    # hour .- Hour std time
    # minute .- Minute std time
    # Long .- Longitude in degrees [0,360] East
    LStd=LongStd( Long)
    DoY=DayOfYear( day, month)
    E=ET( DoY)
    StdTime=HMtoStandardTime( day, month, hour, minute)           
    STime=round(StdTime+4.0*(LStd-Long)+E,0)
    return STime


def SolarTimetoStandardTime( day, month, solartime, Long):
    # day .- Day of the month
    # month .- Month of the year
    # hour .- Hour std time
    # minute .- Minute std time
    # Long .- Longitude in degrees [0,360] East
    LStd=LongStd( Long)
    DoY=DayOfYear( day, month)
    E=ET( DoY)
    StdTime=solartime-4.0*(LStd-Long)-E
    return StdTime
  

def SolarTimetoHourAngle( SolarTime):
    # SolarTime .- Solar time in minutes past midnight
    omega=(SolarTime-720.0)/4.0
    return omega
    

def StandardTimetoHM( standardtime, day, month):
    # hourangle .- Solar time in minutes past midnight
    H=[0,0]
    hour=math.floor( standardtime/60.0)
    minutes=round(standardtime-hour*60.0,0)
    DoY=DayOfYear( day, month)
    start=DayOfYear( 27, 3)
    end=DayOfYear( 30, 10)
    if (DoY>=start) and (DoY<end):
        hour=hour+2
    else:
        hour=hour+1
    H[0]=hour
    H[1]=minutes
    return H    

def HourAngletoSolarTime( HourAngle):
    ST=HourAngle*4.0+720
    return ST


def Theta( day, month, hour, minute, Long, Lat, Azimuth, beta):
    # day .- Day of the month
    # month .- Month of the year
    # hour .- Solar time hour
    # minute .- Solar time minutes
    # Long .- Longitude in degrees [0,360] East
    # Lat .- Latitude in degree [-90,90] 
    # Azimuth .- azimuth of solar panel
    # beta .- slope of the pv panel
    DtR=math.pi/180.0 # Deg to Rad
    DoY=DayOfYear( day, month)
    delta=Declination( DoY)
    ST=hour*60.0+minute
    omega=SolarTimetoHourAngle( ST)
    phi=Lat
    gamma=Azimuth
    A=math.sin(delta*DtR)*math.sin(phi*DtR)*math.cos(beta*DtR)
    B=math.sin(delta*DtR)*math.cos(phi*DtR)*math.sin(beta*DtR)*math.cos(gamma*DtR)
    C=math.cos(delta*DtR)*math.cos(phi*DtR)*math.cos(beta*DtR)*math.cos(omega*DtR)
    D=math.cos(delta*DtR)*math.sin(phi*DtR)*math.sin(beta*DtR)*math.cos(gamma*DtR)*math.cos(omega*DtR)
    E=math.cos(delta*DtR)*math.sin(beta*DtR)*math.sin(gamma*DtR)*math.sin(omega*DtR)
    cos_theta=A-B+C+D+E
    theta=math.acos( cos_theta)/DtR
    return theta
   
   
def SunsetHourAngle( declination, lat):
    DtR=math.pi/180.0 # Deg to Rad
    cos_omega_s=-(math.sin(DtR*declination)*math.sin(DtR*lat))/(math.cos(DtR*declination)*math.cos(DtR*lat))
    omega_s=math.acos( cos_omega_s)/DtR
    return omega_s


def SolarDistance():
    return 1.495e11


def EarthDiameter():
    return 1.27e7


def SunDiameter():
    return 1.39e9







    