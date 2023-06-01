# Ejecutar "python3 test4.py" en la terminal en la carpeta donde se
# encuentra el fichero actividad4.py.

import random

from actividad4 import base2_a_decimal

def remover_ceros(a):             # a = lista de digitos decimales
    n = len(a)
    while n >= 1 and a[n-1] == 0:
        n -= 1
    del a[n:]

e = 0

# test1
e1 = 0
for i in range(100):
    x = random.randint(0,10**i)
    b = list(reversed(list(map(int, list(bin(x)[2:])))))
    d1 = list(reversed(list(map(int, list(str(x))))))
    remover_ceros(b)
    remover_ceros(d1)
    d2 = base2_a_decimal(b)
    if d1 != d2:
        print ('Error en test-1')
        e1 += 1
if e1 == 0:
    print ('Test-1 ok!')
e += e1

# test2
e2 = 0
for i in range(15):
    x = random.randint(0,10**(2**i))
    b = list(reversed(list(map(int, list(bin(x)[2:])))))
    d1 = list(reversed(list(map(int, list(str(x))))))
    remover_ceros(b)
    remover_ceros(d1)
    d2 = base2_a_decimal(b)
    if d1 != d2:
        print ('Error en test-2')
        e2 += 1
if e2 == 0:
    print ('Test-2 ok!')
e += e2

# resultado
if e == 0:
    print('Aprobado!')
else:
    print('Se encontraron', e, 'errores!')
