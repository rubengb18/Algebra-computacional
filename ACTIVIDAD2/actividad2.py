# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 19:45:00 2022

Ruben Gomez Blanco
"""

def conway(l,m,n,k):
    for gen in range(k):
        lista_res=[]
        for i in range(0,m):
            fila=[]
            for j in range(0,n):
                num_vecinos=0
                prim_fila=False
                ult_fila=False
                prim_col=False
                ult_col=False
                if i==0:
                    prim_fila=True
                if i==m-1:
                    ult_fila=True
                if j==0:
                    prim_col=True
                if j==n-1:
                    ult_col=True
                    
                if prim_fila==False and ult_fila==False and prim_col==False and ult_col==False: #Casillas de en medio, contamos los 8 vecinos
                    num_vecinos=l[i-1][j-1] + l[i+1][j-1] + l[i-1][j] + l[i+1][j] + l[i-1][j+1] + l[i][j+1] + l[i+1][j+1] + l[i][j-1]
                if prim_fila==False and ult_fila==False and prim_col==False and ult_col==True: #Casillas de las filas de en medio y ultima columna, no hay vecinos a la der
                    num_vecinos=l[i-1][j-1] + l[i][j-1] + l[i+1][j-1] + l[i-1][j] + l[i+1][j]
                if prim_fila==False and ult_fila==False and prim_col==True and ult_col==False: #Casillas de las filas de en medio y primera columna, no hay vecinos a la izq
                    num_vecinos=l[i-1][j] + l[i+1][j] + l[i-1][j+1] + l[i][j+1] + l[i+1][j+1]
                if prim_fila==False and ult_fila==False and prim_col==True and ult_col==True: #Matriz columna, casillas de las filas de en medio y no hay vecinos a los lados
                    num_vecinos=l[i-1][j]+l[i+1][j]
                if prim_fila==False and ult_fila==True and prim_col==False and ult_col==False: #Casillas de las columnas de en medio y ultima fila, no hay vecinos abajo
                    num_vecinos=l[i-1][j-1] + l[i-1][j] + l[i-1][j+1] + l[i][j+1] + l[i][j-1]    
                if prim_fila==False and ult_fila==True and prim_col==False and ult_col==True: #Esquina inf der
                    num_vecinos= l[i-1][j] + l[i-1][j-1] + l[i][j-1]
                if prim_fila==False and ult_fila==True and prim_col==True and ult_col==False: #Esquina inf izq
                    num_vecinos= l[i-1][j] + l[i-1][j+1] + l[i][j+1] 
                if prim_fila==False and ult_fila==True and prim_col==True and ult_col==True: #Matriz columna, casilla de abajo
                    num_vecinos= l[i-1][j]
                if prim_fila==True and ult_fila==False and prim_col==False and ult_col==False: #Casillas de las columnas de en medio y primera fila, no hay vecinos arriba
                    num_vecinos= l[i+1][j-1] + l[i+1][j] + l[i][j+1] + l[i][j-1] + l[i+1][j+1]   
                if prim_fila==True and ult_fila==False and prim_col==False and ult_col==True: #Esquina superior der
                    num_vecinos= l[i+1][j] + l[i+1][j-1] + l[i][j-1] 
                if prim_fila==True and ult_fila==False and prim_col==True and ult_col==False: #Esquina superior izq
                    num_vecinos= l[i+1][j] + l[i+1][j+1] + l[i][j+1]    
                if prim_fila==True and ult_fila==False and prim_col==True and ult_col==True: #Matriz columna, casilla de arriba
                    num_vecinos= l[i+1][j]      
                if prim_fila==True and ult_fila==True and prim_col==False and ult_col==False: #Matriz fila, casillas del medio y no vecinos arriba ni abajo
                   num_vecinos= l[i][j+1]+l[i][j-1]
                if prim_fila==True and ult_fila==True and prim_col==False and ult_col==True: #Matriz fila, casilla de la derecha
                   num_vecinos=l[i][j-1]
                if prim_fila==True and ult_fila==True and prim_col==True and ult_col==False: #Matriz fila, casilla de la izquierda
                   num_vecinos=l[i][j+1]
                #Regla 1:Las celdas vacias rodeadas por exactamente tres individuos tendran un individuo en la siguiente generacion
                if l[i][j] == 0 and num_vecinos == 3:
                    fila.append(1)
                #Regla 2: Una celda viva con menos de 2 o 3 vecinas vivas, "muere".
                elif l[i][j] == 1 and (num_vecinos < 2 or num_vecinos > 3):
                    fila.append(0)
                else:   #En caso contrario se queda igual
                    fila.append(l[i][j])                   
            lista_res.append(fila)
        l=lista_res
    return l        
