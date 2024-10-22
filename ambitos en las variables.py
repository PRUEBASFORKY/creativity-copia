G = "Esta variable es de ámbito Global"
def f1():
    E= "Esta variable es local de la función F1. Enclosing a F2"
    print (E)
    def f2():
        L = "Esta variable es local a f2"
        print(L, E, G, sep = "\n")
        f2()
        print (L)

f1()
print (G)

