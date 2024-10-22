def f(a,b,c, d):
    print(a,b,c,d)
argumentos = {'b':20, 'a':1, 'c':300, 'd':4000}
f(**argumentos)

argumentos = {'b':200, 'c':300, 'd':400}
f(10, **argumentos)
