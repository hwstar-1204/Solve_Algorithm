#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    left_to_right, right_to_left = 0, 0
    
    for i in range(n):
        for j in range(n):
            if i == j:
                left_to_right += arr[i][j]
            elif i+j == n-1:
                right_to_left += arr[i][j]
    
    if n % 2:
        left_to_right -= arr[i//2][j//2]
        
    result = left_to_right - right_to_left

    return abs(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
