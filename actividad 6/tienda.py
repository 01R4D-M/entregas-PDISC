from matematica.contable import *
from os import system

system("cls")

suma = 0

print("Tienda Virtual".center(50, "-")+"\n")

prod = ["alfajores", "Frascos de mermelada", "Latas de atun", "Botellas de gaseosa"]

precios = [30, 50, 100, 150]

for i in range(len(prod)):
    cant = int(input("Ingrese la cantidad de "+ str(prod[i]) + " que desea comprar: "))
    suma += cant * precios[i]

print("\nEl precio total a pagar por todos los productos es: $"+ str(incremento(suma, 21)))
