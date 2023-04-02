#!/bin/python3

import math
import os
import random
import re
import sys
import datetime 

def timeConversion(s):
    time_data = s.split(":")                 # once you split the time_data with ":" as a parameter, you divide it into 12, 01 and 00PM. 
    hours = int(time_data[0])                # now you just assign them to a variable as an integer.
    minutes = int(time_data[1])              
    seconds = int(time_data[2][:2])          # here we are removing the "PM" part of the "00PM".
    period = time_data[2][2:]                # here we are removing the "00" part of the "00PM".

    if period == "PM" and hours != 12:       # this is an if condition where we are taking some conditions into consideration, whicha are again mentioned in the description of the problem.
        hours += 12
    elif period == "AM" and hours == 12:
        hours = 0

    return "{0:02d}:{1:02d}:{2:02d}".format(hours, minutes, seconds)   # here we're giving some padding and printing the results in a 24 hour format.


# checking to see if everything is working.

n = "12:01:00PM"
print(timeConversion(n))
