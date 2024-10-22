def factorial(x):
    print(x)
    if x>1:
        return x*factorial(x-1)
    else:
        return 1
   
factorial(3)
