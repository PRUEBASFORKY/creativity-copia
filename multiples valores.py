def maxmin(lista):
    return max(lista), min(lista)

l= [1,3,5,6,0]
maximo, minimo = maxmin(l)

print(minimo, maximo, sep= "")