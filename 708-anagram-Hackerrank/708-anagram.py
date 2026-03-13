#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    n = len(s)
    if n%2 != 0:
        return -1
    s1 = s[:n//2]
    s2 = s[n//2 :]
    char_count = {}
    for i in s1:
        char_count[i] = char_count.get(i,0)+1
    for i in s2:
        if i in char_count and char_count[i]>0:
            char_count[i] -= 1
    return sum(char_count.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
