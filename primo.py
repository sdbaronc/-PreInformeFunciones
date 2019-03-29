def primo():
    n=int(input("ingrese un numero"))
    cont=0
    for x in range(1,n+1):
        if n%x==0:
            cont += 1
    if cont>2:
        print("el nomero no es primo")
    else:
        print("el numero es primo")
primo()