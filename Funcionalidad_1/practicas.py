num = int(input("Ingrese un numero entero positivo entre 1 y 10"))
cont = 1


if num >= 1 and num <= 10:
    for  cont in range(1,11):

        
        print(f"{num} * {cont} = ", num * cont)
        

else:
        print("Ingrese un numero valido")    