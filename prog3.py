menu = print("""S. Suma
R. Restra
M. Multiplicacion
D. Division
A. Salir""")


opc = input("Elija una opcion. ")


while opc.upper() in "SRMDA":
    if opc.upper() == "S":
        num1 = int(input("Primer numero: "))
        num2 = int(input("Segundo numero"))
        suma = num1 + num2
        print(f"la suma es {suma}")
    
    
    elif opc.upper() == "R":
        num1 = int(input("Primer numero: "))
        num2 = int(input("Segundo numero"))
        resta = num1 - num2
        print(f"la resta es {resta}")
    
    elif opc.upper() == "M":
        num1 = int(input("Primer numero: "))
        num2 = int(input("Segundo numero"))
        multi = num1 - num2
        print(f"la multiplicacion es {multi}")
    
    elif opc.upper() == "D":
        num1 = int(input("Primer numero: "))
        num2 = int(input("Segundo numero"))
        division = num1 - num2
        print(f"la divison es {division}")
    
else:
    print("salir")
