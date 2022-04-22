from matematica.aritmetica import *
from matematica.contable import *
from matematica.geometria import *

print("MENU".center(50, "-")+"\n")

print("1. Porcentaje")
print("2. Descuento")
print("3. Incremento")
print("4. Aporte jubilatorio")
print("5. Aporte a la obra social")
print("6. Aporte al sindicato")
print("7. Promedio")
print("8. Valor en 12 coutas sin interes")
print("9. Valor en coutas con interes prefijado")
opc = int(input("Ingrese la opcion del calculo que desea realizar: "))

if opc == 1:
    total = int(input("Ingrese el numero equivalente a 100%: "))
    porcent = int(input("Ingrese el procentaje a calcular: "))
    print("El", porcent+"% de", total, "es:", porcentaje(total, porcent))
elif opc == 2:
    total = int(input("Ingrese el valor total: "))
    porcent = int(input("Ingrese el porcentaje de descuento a aplicar: "))
    print("El valor con el descuento aplicado es:", descuento(total, porcent))
elif opc == 3:
    total = int(input("Ingrese el valor total: "))
    porcent = int(input("Ingrese el porcentaje de incremento a aplicar: "))
    print("El valor con el descuento aplicado es:", incremento(total, porcent))
elif opc == 4:
    total = int(input("Ingrese el sueldo total: "))
    print("El valor del aporte jubilatorio es:", jubilacion(total))
elif opc == 5:
    total = int(input("Ingrese el sueldo total: "))
    print("El valor del aporte a la obra social es:", obraSocial(total))
elif opc == 6:
    total = int(input("Ingrese el sueldo total: "))
    print("El valor del aporte al sindicato es:", sindicato(total))
elif opc == 7:
    lista = []
    n = int(input("Ingrese cuantos numeros desea promediar: "))
    for i in range(n):
        a = int(input("Ingrese el "+ str(i+1) + "° numero: "))
        lista.append(a)
    print("El promedio de todos los numeors es:", promedio(lista))
elif opc == 8:
    total = int(input("Ingrese el valor total a pagar: "))
    print("el valor de cada cuota es:", doceCuotas(total))
elif opc == 9:
    total = int(input("Ingrese el valor total: "))
    cant = int(input("Ingrese la cantidad de cuotas: "))
    print("el valor de cada cuota es:", cuotas(total, cant))