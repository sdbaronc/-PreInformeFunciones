def impar():
    n=int(input("ingrese el ultimo valor del rango: "))
    for x in range(1,n+1):
        if x %2!=0:
            print(x)
impar()