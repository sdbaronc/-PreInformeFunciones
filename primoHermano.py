def primoH():
    n=int(input("ingrese un numero: "))
    if n%6==0:
        print("no es primo hermano")
    else:
        b=n+1
        cont = 0
        for x in range(1, b + 1):
            if b % x == 0:
                cont += 1
        if cont<3:
            print("el numero es primo hermano")
primoH()