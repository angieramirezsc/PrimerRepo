num1 = int(input("Dame un numero: "))
num2 = int(input("Escribe otro: "))
suma = 0
for numero in range(num1,num2+1,1):
    suma += numero
    

print(f'la suma es {suma}')
