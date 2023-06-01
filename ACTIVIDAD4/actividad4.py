# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 18:31:08 2022

@author: Ruben

"""

from natural import *

def calcula_potencias_hasta_n(n):
    dicc={}
    dicc[0]=[1]
    dicc[1]=[2]
    i=2
    while i<n:
        dicc[i]= multiplicar_karatsuba(dicc[i//2],dicc[i//2])
        i=i*2
    return dicc
        
def comprueba_y_rellena_lista(a):   #Relleno con los 0s suficinetes para tener una lista de tamaño potencia de 2
    cont=0
    tam=len(a)
    while tam>=2**cont:
        cont=cont+1
    n=2**cont
    for i in range(0,n-tam):
        a.append(0) 

def base2_a_decimal_d(a,dicc):
    if len(a)==1:
        return a
    a.append(0) #Para que haya uno en medio facil de coger
    n=len(a)//2
    dos_elevado_a_n=dicc[n]
    dos_elevado_a_n_mas_1=[]
    if n+1 in dicc:
        dos_elevado_a_n_mas_1=dicc[n+1]   
    else:
        dos_elevado_a_n_mas_1=multiplicar_karatsuba(dos_elevado_a_n,[2])
        dicc[n+1]=dos_elevado_a_n_mas_1

    if a[n]==1:
        return sumar(dos_elevado_a_n,sumar(base2_a_decimal_d(a[0:n],dicc),multiplicar_karatsuba(base2_a_decimal_d(a[n+1::],dicc),dos_elevado_a_n_mas_1)))
    else:
        return sumar(base2_a_decimal_d(a[0:n],dicc),multiplicar_karatsuba(base2_a_decimal_d(a[n+1::],dicc),dos_elevado_a_n_mas_1))
    

def  base2_a_decimal(a):
    if a==[]:
        return a
    comprueba_y_rellena_lista(a)
    potencias=calcula_potencias_hasta_n(len(a))
    return base2_a_decimal_d(a,potencias)
    



