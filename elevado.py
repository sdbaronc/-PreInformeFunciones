def potencias():
    a=int(input("ingrese la base de el primer numero: "))
    b=int(input("ingrese la potencia del primer numero: "))
    c = int(input("ingrese la base de el segundo numero: "))
    d = int(input("ingrese la potencia del segundo numero: "))
    x1= a**b
    x2=c**d
    print("la potencia del primer numero es:" , x1)
    print("la potencia del segundo numero es:", x2)
    if x1>x2:
        print(x1,">",x2)
    elif x2>x1:
        print(x2,">",x2)
    else:
        print(x1,"y",x2,"son iguales")
potencias()

