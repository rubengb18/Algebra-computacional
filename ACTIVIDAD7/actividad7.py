# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 15:29:41 2022

@author: Ruben Gomez Blanco
"""

import math
import random

"""Calculo los primos anterores a 3*N con eratostenes, y luego hago una funcion factorizar para quedarme solo 
con los primos de esa lista de eratostenes que dividan a mi numero.
Con esa lista de factores primos es con la que hago el test de Lucas.
"""

def eratostenes_mio(x):
    numeros = list(range(2,x+1))
    d=0
    while numeros[d]**2 <= x:
        for n in numeros:
            if n != numeros[d]:
              if n % numeros[d] == 0:
                numeros.remove(n)
        d += 1
    return numeros

N=2000  #Hasta donde quiera mirar
numeros_primos=eratostenes_mio(3*N) 

def factorizar(resultado,n):
    i=0
    while n != 1:
        if n % numeros_primos[i] == 0:
            resultado.add(numeros_primos[i])
            n = n / numeros_primos[i]
        else:
            i+=1
    return resultado

def p(m):
    total=1
    posibles_factores_primos=set()
    for i in range(m):
        prod=(3*i)+1
        total*=prod
        posibles_factores_primos=factorizar(posibles_factores_primos,prod)
    return posibles_factores_primos,total

def es_primo_rabin_miller (N, num_intentos):
    if N in { 2 , 3 , 5 , 7 }:
        return True
    if N < 11:
        return False
    if N % 2 == 0:
        return False
    r = 0
    m = N -1
    while m % 2 == 0:
        m //= 2
        r += 1
    for i in range(num_intentos):
        a = random.randint (1, N-1)
        if math.gcd(a, N) != 1:
            return False
        x = pow(a, m, N)
        esta_en_T_N = (x == 1) or (x == N-1)
        t = 0
        while not esta_en_T_N and t < r-1:
            x = pow(x, 2, N)
            esta_en_T_N = (x == N-1)
            t += 1
        if not esta_en_T_N :
            return False
    return a,True

def es_primo_lucas(factores_primos,n):

    if n in { 2 , 3 , 5 , 7 }:
        return True
    if n < 11:
        return False
    if n % 2 == 0:
        return False
    for primo in factores_primos:
        if primo % (n-1) == 0: ###Si es factor primo
            encontrado=False
            for a in range(2,n):
                if pow(a,n-1,n)==1 and pow(a,int((n-1)/primo),n)!=1:
                    encontrado=True
                    break
            if encontrado==False:
                return False
    return True

def test_pm_plus_1(m):
   factores_primos,n=p(m)
   n+=1
   if es_primo_rabin_miller(n, 10):
       if es_primo_lucas(factores_primos,n):
           return True
       else:
           return False
   else:
       return False

def test():
    for m in range(1,N):
        print("Probando "+str(m)+'\n')
        res=test_pm_plus_1(m)
        if res==True:
            print(m)
    

#Para probar con los 2000
#print(test())
print(test_pm_plus_1(1))
print(test_pm_plus_1(2))
print(test_pm_plus_1(3))
print(test_pm_plus_1(4))
print(test_pm_plus_1(14))
print(test_pm_plus_1(20))
print(test_pm_plus_1(31))
print(test_pm_plus_1(59))
print(test_pm_plus_1(443))
print(test_pm_plus_1(1600))
print(test_pm_plus_1(1659))