num = int(input("Ingrese un numero entero positivo"))



if num > 0:
    for num in range(num,-1, -1):
        if num % 2 == 0 :
            print(str(num) + " ", end= " ")


