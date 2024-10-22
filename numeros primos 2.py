# Para implementar una calculadora de números primos en Python, 
# lo primero es saber si dos números son divisibles. Usamos el operador módulo %.

D = 3
d = 1

if D%d != 0:
    print("No es divisor", D)

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
        print("Es primo")
        return True
    
es_primo(13)
es_primo(14)
es_primo(887)
es_primo(4)