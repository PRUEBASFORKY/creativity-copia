# a = input ("Introduce un número: ")
# texto = input ("Introduce algo por el teclado: ")

l = list() #creamos lista vacía
texto = input ("Introduce un número entero por teclado: ")
if texto.isnumeric():
    num = int(texto)
    l.append(num)
    print("Número " + str(num) + " añadido a la lista")
else:
    print("No has introducido un número entero")
6