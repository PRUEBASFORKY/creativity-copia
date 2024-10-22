d = { "50862634" : 37 , "43394932" : 32} #creamos diccionario

texto = input("Introduce un documento de identidad: ")

if texto in d: #comprobamos si esta en el diccionario
    print("La edad de " + texto + " es " + str(d[texto]))
else:
    edad = input("Documento no existente. Introduce edad: ")
    if edad.isnumeric():
        num = int(edad)
        d[texto] = num
        print("Añadido al diccionario")
print(d) #Mostramos por pantalla el diccionario