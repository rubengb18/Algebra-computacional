import actividad6 as act

# test-1
if act.f(1,3) == 187:
    print('test-1: ok')
else:
    print('test-1: error')

# test-2
if act.f(3,4) == 9627:
    print('test-2: ok')
else:
    print('test-2: error')

# test-3
if act.f(2022,10) == 4398470083:
    print('test-3: ok')
else:
    print('test-3: error')

# test-4
if act.f(5**100,100) == 3885498536840880390558163388239328561791403020448934831005492927806052986760687686813792112667714187:
    print('test-4: ok')
else:
    print('test-4: error')

