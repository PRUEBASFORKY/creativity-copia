a= False
b= True

resultado = a and b
print (resultado)

resultado = a or b
print (resultado)

resultado = not a
print (resultado)

edad = int(input('Introduce tu edad:'))
if(20 >= edad < 30) or(30 <= edad <40):
    print('Dentro del rango (20\'s) o (30\'s)' )
else:
    print("No estas dentro del rango de los 20's ni 30's")