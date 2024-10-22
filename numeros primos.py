def factores(lista):
    return primos (lista), compuestos (lista)

l = [1,2,4,5,6,8]
primos, compuestos = factores(l)

print(compuestos, primos, sep= " ")