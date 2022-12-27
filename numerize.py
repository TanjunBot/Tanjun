#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from decimal import Decimal

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

def numerize(n):
    num = int(n)
    magnitude = 0

    strnum = str(num)
    listnum = list(strnum)

    while abs(num) >= 1000:
        magnitude += 1
        listnum = listnum[:-1]
        listnum = listnum[:-1]
        listnum = listnum[:-1]
        strnum = ""
        for l in listnum:
            strnum += l
        #print(strnum)
        if strnum == "":
            strnum = "0"
        num = int(strnum)
        #num = int(num / 1000)
    # add more suffixes if you need them

        





print(numerize(100000))