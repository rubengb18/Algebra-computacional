# Ejecutar "python3 test3.py" en la terminal en la carpeta donde se
# encuentra el fichero actividad3.py.

from actividad3 import es_suma_de_k_potencias_n

e = 0

# test1 (0<=x<100, k=2, n=2)
l1 = [True, True, True, False, True, True, False, False, True, True, True, False, False, True, False, False, True, True, True, False, True, False, False, False, False, True, True, False, False, True, False, False, True, False, True, False, True, True, False, False, True, True, False, False, False, True, False, False, False, True, True, False, True, True, False, False, False, False, True, False, False, True, False, False, True, True, False, False, True, False, False, False, True, True, True, False, False, False, False, False, True, True, True, False, False, True, False, False, False, True, True, False, False, False, False, False, False, True, True, False]
l2 = [es_suma_de_k_potencias_n(x, 2, 2) for x in range(100)]
if l1 != l2:
    print ('Error en test-1')
    e += 1
    
else:
    print ('Test-1 ok!')

# test2 (0<=x<100, k=3, n=2)
l1 = [True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, False, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, False, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, False, True, True, True, True]
l2 = [es_suma_de_k_potencias_n(x, 3, 2) for x in range(100)]
if l1 != l2:
    print ('Error en test-2')
    e += 1
else:
    print ('Test-2 ok!')

# test3 (0<=x<100, k=2, n=3)
l1 = [True, True, True, False, False, False, False, False, True, True, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False]
l2 = [es_suma_de_k_potencias_n(x, 2, 3) for x in range(100)]
if l1 != l2:
    print ('Error en test-3')
    e += 1
else:
    print ('Test-3 ok!')

# test4 (0<=x<100, k=6, n=3)
l1 = [True, True, True, True, True, True, True, False, True, True, True, True, True, True, False, False, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, False, False, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, False, True, False, True, True, True, True, True, True, True, True, True, True, True, True]
l2 = [es_suma_de_k_potencias_n(x, 6, 3) for x in range(100)]
if l1 != l2:
    print ('Error en test-4')
    e += 1
else:
    print ('Test-4 ok!')

# test5 (x = 8**10 + 13*(7**10) + 1, k = 15, n = 10)
x = 8**10 + 13*(7**10) + 1
if not es_suma_de_k_potencias_n(x, 15, 10):
    print ('Error en test-5')
    e += 1
else:
    print ('Test-5 ok!')

# test6 (x = 8**10 + 13*(7**10) + 1, k = 14, n = 10)
x = 8**10 + 13*(7**10) + 1
if es_suma_de_k_potencias_n(x, 14, 10):
    print ('Error en test-6')
    e += 1
else:
    print ('Test-6 ok!')

# resultado
if e == 0:
    print('Aprobado!')
else:
    print('Se encontraron', e, 'errores!')
