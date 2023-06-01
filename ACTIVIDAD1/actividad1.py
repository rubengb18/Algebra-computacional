"""
Ruben Gomez Blanco
"""

def eliminar5(n):
    indice=1;
    resultado=0
    valor_abs=abs(n)
    while valor_abs>0:
        cifra=valor_abs%10
        if cifra!=5:
            resultado=resultado+indice*cifra
            indice=indice*10
        valor_abs=valor_abs//10
    if n<0:
        resultado=resultado*(-1)
    return resultado            
            
    
