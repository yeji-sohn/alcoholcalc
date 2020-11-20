#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 10:36:00 2020

@author: sohn-yeji
"""

#alchol unit calculator using Widmark formula.

#input
def AskForDetails():
    beer = float(input("Number of pint(s) of beer or cider(5% ABV) consumed: "))
    wine = float(input("Number of glass(es) of wine(12% ABV) consumed: "))
    shot = float(input("Number of shot(s) of spirits(40% ABV) consumed: "))
    weight = float(input("Enter you body weight in kg: "))
    weight = weight * 1000
    gender = input("if you are a male type M if you are a female type F: ")
    if gender == "F" or gender == "f":
        R = float(0.55)
    elif gender == "M" or gender =="m":
        R = float(0.68)
    time = float(input("How many hours has passed since you started drinking: "))
    
    return beer, wine, shot, weight, gender, R, time

#total units of alchol comsumed 
def total_unit( beer, wine, shot ):
    beerunit = beer * 2.8
    wineunit = wine * 2.1
    shotunit = shot * 1
    total_unit = beerunit + wineunit + shotunit
    total_unit = round(total_unit,2)
    T_unit = float(total_unit)
    
    return T_unit

#Calculate BAC( Bood Alcohol Concentration )
#one unit equals to 10ml or 8g of pure alcohol
#account for the elapsed time and the amount of alcohol that your body has
#already metabolized by the time you calculate your BAC hence (time*0.015)

def BAC( T_unit, weight, R, time ):
    BAC = ( ( T_unit * 8 )/( weight * R ) ) * 100 - ( time * 0.015 )
    BAC = round(BAC,2)
    BAC_now = float(BAC)
    
    return BAC_now

#estimated time for the BAC to drop to 0 from now

def SoberUp(T_unit, weight, R, time ):
    SoberUp = ((T_unit * 8)/( weight * R ))* 100 / 0.015 - time
    SoberUp = round(SoberUp, 1)
    
    return SoberUp
    
#Output
def Information():
    beer, wine, shot, weight, gender, R, time = AskForDetails()
    T_unit = total_unit(beer, wine, shot)
    BAC_now = BAC(T_unit, weight, R, time)
    
    print("----------------------------------------------------------------")
    print("You have consumed", total_unit(beer, wine, shot ),\
          "unit(s) of alcohol and your current estimation BAC is",\
              BAC( T_unit, weight, R, time ),"%. It will take up to another",\
                  SoberUp( T_unit, weight, R, time ), "hours to completely"\
                      " detoxicate yourself")
    if 0.04 > BAC_now > 0.02:
        print("Most people begin to feel relaxed")
    elif 0.07 > BAC_now > 0.04:
        print("Judgment is somewhat impaired")  
    elif 0.1 > BAC_now > 0.07:
        print("Most people experience definite impairment of muscle"\
              " coordination and driving skills. now you're legally drunk")
    elif 0.3 > BAC_now > 0.2:
        print("!WARNING! Most people begin to experience blackouts"\
              " at your level of BAC")
    elif 0.4 > BAC_now > 0.3:
        print("!WARNING! Most people begin to experience blackouts"\
              " at your level of BAC")
    elif 0.5 > BAC_now > 0.4:
        print("!WARNING! This is a fatal dose for most people.")


Information()


