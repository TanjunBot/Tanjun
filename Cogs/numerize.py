#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

import sys
from decimal import Decimal
import time
start = time.time()

sys.setrecursionlimit(100000)

def round_num(n, decimals):
    """
    Params:
    n - number to round
    decimals - number of decimal places to round to
    Round number to 2 decimal places
    For example:
    10.0 -> 10
    10.222 -> 10.22
    """
    return n.to_integral() if n == n.to_integral() else round(n.normalize(), decimals)

def drop_zero(n):
    """
    Drop trailing 0s
    For example:
    10.100 -> 10.1
    """
    n = str(n)
    return n.rstrip("0").rstrip(".") if "." in n else n


def shortennumber(number):
    length = len(str(number))
    times = 0
    lenx = int(length)
    while lenx - 26 >= 0:
        times += 1
        lenx -= 26
    suffix = ""
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v" ,"w","x","y", "z"]
    while times != 0:
        suffix += alphabet[lenx]
        times -= 1


    print(suffix)



def numerize(n = 0):

    print("Ok..")
    print(n)
    num = int(n)
    magnitude = 0

    strnum = str(num)
    listnum = list(strnum)

    print(len(strnum))

    print(math.ceil(len(strnum) / 3 - 1))

    suffix = suffixes[math.ceil(len(strnum) / 3 - 1)]

    nums = len(strnum) % 3

    print(nums)

    try:
        _ = listnum[0]
    except:
        listnum.append("0")
    
    try:
        _ = listnum[1]
    except:
        listnum.append("0")

    try:
        _ = listnum[2]
    except:
        listnum.append("0")


    try:
        _ = listnum[3]
    except:
        listnum.append("0")

    try:
        _ = listnum[4]
    except:
        listnum.append("0")

    if nums == 0:
        number = f"{listnum[0]}{listnum[1]}{listnum[2]}.{listnum[3]}{listnum[4]} {suffix}"
    elif nums == 2:
        number = f"{listnum[0]}{listnum[1]}.{listnum[2]}{listnum[3]} {suffix}"
    elif nums == 1:
        number = f"{listnum[0]}.{listnum[1]}{listnum[2]} {suffix}"

    end = time.time()
    print(format(end-start))

    return number

    


def getsuffixes():
    return 




print(shortennumber(545646894654548946541488869846486465645465645645456465645645645645645645))
print(numerize(545646894654548946541488869846486465645465645645456465645645645645645645))