nombre = input("Ingrese su nombre completo: ")
horas = int(input("Ingrese la cantidad de horas trabajadas: "))
valor = float(input("Ingrese el valor hora del operario: "))
sueldo = horas * valor
print("El sueldo bruto de", nombre, "es", sueldo)