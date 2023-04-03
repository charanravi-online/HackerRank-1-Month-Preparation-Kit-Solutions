#!/bin/python3

import math
import os
import random
import re
import sys


def matchingStrings(strings, queries):
    output_list = []                           # we're creating an output list that we would be printing in the end
    for query in queries:                      # in this nested for loop, we are trying to compare the contents present in the string with the query.
        count = 0                              # if there is a match, we are incrementing the count variable.
        for string in strings:                 # and we are appending the count value to the list we created first.
            if query == string:
                count +=1
        output_list.append(count)
    return output_list                         # returning the list with all the count values.


strings = ['ab','ab','abc']
queries = ['ab', 'abc','bc']
print(matchingStrings(strings, queries))
            

