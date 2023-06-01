# -*- coding: utf-8 -*-
"""
@author: Rubén Gómez Blanco
"""

def raiz_nesima_super_rapida (x,n): 
     izq = 0
     der = x+1
     while izq < der -1:
        med = (izq+der )//2
        if med **n <= x:
            izq = med
        else :
            der = med
     return izq

"""
Idea intuitiva:
La idea es hacer la raiz enesima de x y quedarnos con su parte entera, si al elevar esta raiz a n es x, entonces ya lo tenemos.
Si no le restamos esta potencia al total x y llamamos recursivamente a la funcion decrementanto la k.
Tenemos un diccionario para ir llevando los numeros (como claves) y la k (como valor) que ya sabemos que es imposible hacerlo, 
para en posibles futuras iteracion no volver a comprobarlo.
Ahora, si con esa raiz enesima no se puede, la decrementamos en una unidad y probamos otra vez con otra combinacion.
"""
def es_suma_de_k_potencias_n(x,k,n):
    dicc={}
    return es_suma_de_k_potencias_n_rec(x,k,n,dicc)

def es_suma_de_k_potencias_n_rec(x,k,n,dicc):
    if(x==0):
        return True
    raiz_nesima_x=raiz_nesima_super_rapida (x,n)
    res=False
    if x in dicc:
        if dicc[x]==k:
            return False
    for i in range(int(raiz_nesima_x),0,-1):
        if k>0:
            if pow(raiz_nesima_x,n)==x:
                return True
            else:
                suma=pow(i,n)
                res= es_suma_de_k_potencias_n_rec(x-suma,k-1,n,dicc)
                if res==True:
                    return True
                else:
                    dicc[x]=k
    return res
