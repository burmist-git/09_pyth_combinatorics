#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Date        : Fri Dec  4 13:54:00 CET 2020
Autor       : Leonid Burmistrov
Description : Simple reminder-training example.

'''

import numpy as np
from itertools import combinations

def printinfo(func):
    def wrapper():
        print("")
        print("Simple reminder-training example. Function name : {} --> ".format(func.__name__))
        func()
    return wrapper

@printinfo
def combinations_test(vMin=0,vMax=5,n=3):
    print('C_n^k = n!/k!/(n-k)!')
    val=list(range(vMin,vMax))
    print(val)
    for permu in combinations(val, n):
        print(permu)
        
def main():
    combinations_test()
    
if __name__ == "__main__":
    main()
