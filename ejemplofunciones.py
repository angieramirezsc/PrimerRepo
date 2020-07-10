
def repetir(texto,num):
    texto += "\n"
    print(texto*num)

t = input("Ingrese un texto: ")
n = int(input("Veces que desea repetir: "))

repetir(t,n)