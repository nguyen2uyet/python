
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    binary_number = bin(n)[2:]
    max1 = 0
    max2 = 0
    for i in range(len(binary_number)):
        if binary_number[i] == '1':
            max2 += 1
            print("Max2 = {}".format(max2))
            if max1 < max2:
                max1 = max2
        else:
            max2 = 0
            
    print(max1)