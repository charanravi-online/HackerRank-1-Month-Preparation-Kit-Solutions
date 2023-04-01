#!/bin/python3

import math
import os
import random
import re
import sys


# this might sound pretty complex but if you just break it downn into smaller tasks that needs to be taken care of, its really a simple solution


def miniMaxSum(arr):
    arr.sort()                   # sort the given input array and notice how simple it becomes.
                                 # since you're sorting it, half your work is done since now you know where the smallest digit and largest digits reside.
                                 # using this information you can now proceed. As the number of elements in the array is already specified in the problem statement,
                                 # you dont need to do much work here.  
    
    
    min_sum = sum(arr[:4])       # sum(arr) will add all the elements in that array. so we are just addin the elemets we need and storing in a varible min_sum 
    max_sum = sum(arr[1:])       # the same thing for max_sum. Notice how we are just using the list structure since we know how many elements are gonna be there.
    print(min_sum, max_sum)      # we finally print our data.


# and we're done!

n = [1,3,5,7,9]
miniMaxSum(n)
