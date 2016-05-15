# -*- coding: utf-8 -*-
"""
Created on Sun May 15 15:20:18 2016

@author: mananam
"""

import pvsystems as pv
import math

day=15
month=5
DoY=pv.DayOfYear( day, month)
print("day: " + str(day) + "; month: " + str(month) + "=> day of year: " + str(DoY))

delta_d=pv.Declination( DoY)
print("declination: %.1f" % delta_d + " degrees")

ET=pv.ET( DoY)
print("Error time: %.2f" % ET + " minutes")

# Santander
# 43º28' North 
lat=43.0+28.0/60.0
# 3º49' West
lon=-3.0+49.9/60.0
print("*********************************")
print("SUNRISE")
omega_sunrise=-pv.SunsetHourAngle( delta_d, lat)
print("sunrise hour angle: %.2f" % omega_sunrise + " degree")
solartime_sunrise=pv.HourAngletoSolarTime( omega_sunrise)
print("sunrise solar time: %.2f" % solartime_sunset + " minutes")
stdtime_sunrise=pv.SolarTimetoStandardTime( day, month, solartime_sunrise, lon)
print("sunrise standard time: %.2f" % stdtime_sunrise + " minutes")
HM_sunrise=pv.StandardTimetoHM( stdtime_sunrise, day, month)
minutes=round(HM_sunrise[1],0)
print("sunrise hour: %.0f" % (HM_sunrise[0]) + ":" + str(int(minutes)).zfill(2) )

print("*********************************")
print("SUNSET")
omega_sunset=-omega_sunrise
print("sunset hour angle: %.2f" % omega_sunset + " degree")
solartime_sunset=pv.HourAngletoSolarTime( omega_sunset)
print("sunset solar time: %.2f" % solartime_sunset + " minutes")
stdtime_sunset=pv.SolarTimetoStandardTime( day, month, solartime_sunset, lon)
print("sunset standard time: %.2f" % stdtime_sunset + " minutes")
HM_sunset=pv.StandardTimetoHM( stdtime_sunset, day, month)
minutes=round(HM_sunset[1],0)
print("sunset hour: %.0f" % (HM_sunset[0]) + ":" + str(int(minutes)).zfill(2) )


print("*********************************")

DtR=math.pi/180.0
a=math.sin(delta_d*DtR)*math.sin(lat*DtR)/(math.cos(delta_d*DtR)*math.cos(lat*DtR))
print("cos omega_s: %.2f" % a)
b=math.acos(a)/DtR
print("omega_s: %.2f" % b)