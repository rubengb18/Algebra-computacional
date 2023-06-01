# Ejecutar "python3 test1.py" en la terminal en la carpeta donde se
# encuentra el fichero actividad1.py.



from actividad1 import eliminar5

e = 0

casos = [(-5152, -12), (5, 0), (15, 1), (0, 0), (1, 1), (10, 10), (-555, 0), (252525, 222), (-755577555557, -7777)]
n = len(casos)

# test-1
i = 0
while i < n:
    x,y = casos[i]
    z = eliminar5(x)
    if y != z:
        print('error en test-1: eliminar5(', x, ') devolvió', z, 'pero lo correcto es', y)
        e += 1
    i += 1

# test-2
i = 20
while i <= 300:
    x = 5*(10**i-1)//9 - 10**(i//3) + 1
    y = 46
    z = eliminar5(x)
    if y != z:
        print('error en test-2: eliminar5(', x, ') devolvió', z, 'pero lo correcto es', y)
        e += 1
    x = -x
    y = -y
    z = eliminar5(x)
    if y != z:
        print('error en test-2: eliminar5(', x, ') devolvió', z, 'pero lo correcto es', y)
        e += 1    
    i += 1

# resultado
if e == 0:
    print('aprobado!')
else:
    print('se encontraron', e, 'errores!')
