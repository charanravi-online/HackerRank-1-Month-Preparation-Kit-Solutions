#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    n = len(arr)                                  #get how many elements exist in the array
    negative_num = 0                              #initialize negative_num = 0
    zero_num = 0                                  #initialize zero_num = 0
    positive_num = 0                              #initialize positive_num = 0
    for num in arr:                               
        if num > 0:
            positive_num += 1                     #if positive number is found in the loop, positive_num gets appende to 1. 
        elif num < 0:               
            negative_num += 1                     #if negative number is found in the loop, negative_num gets appended to 1.
        elif num == 0:
            zero_num += 1                         #if zero number is found in the loop, well... you get the point!

    # in the below print statement, we are printing the raios of positive, neagative and zero numbers. 
    # remember n? well we're using it here.

    print(str(positive_num/n),"\n" + str(negative_num/n), "\n"  + str(zero_num/n))  
    


    
# a call to verif our results locally.

a = [1,1,0,-1,-1]
plusMinus(a)
