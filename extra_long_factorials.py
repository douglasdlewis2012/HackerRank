#!/bin/python3
#https://www.hackerrank.com/challenges/extra-long-factorials/problem

import sys
import operator
import functools

def extraLongFactorials(n):
    # Complete this function
    print(functools.reduce(operator.mul, [i for i in range(1,n+1)], 1))

if __name__ == "__main__":
    n = int(input().strip())
    extraLongFactorials(n)
