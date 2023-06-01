# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 20:15:04 2022

@author: Ruben Gomez Blanco
"""

import modular as mdlr

def f(n,m):
    modulo=10**m
    exp=mdlr.potencia_mod(7,n,modulo)
    num=mdlr.potencia_mod(3,exp,modulo)
    return num


print(5**100)
print(f(7888609052210118054117285652827862296732064351090230047702789306640625,60))