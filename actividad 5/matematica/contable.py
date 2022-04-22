def porcentaje (a, b):
    return (a / 100) * b

def descuento (a, b):
    c = porcentaje(a, b)
    return a - c

def incremento (a, b):
    c = porcentaje(a, b)
    return a + c

def jubilacion (a):
    return porcentaje(a, 11)

def obraSocial (a):
    return porcentaje(a, 3)

def sindicato (a):
    return porcentaje(a, 1)

def promedio(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma / len(lista)

def doceCuotas (a):
    return a / 12

def cuotas(a, n):
    if n <= 3:
        return a / n
    elif n <= 6:
        return incremento(a, 15) / n
    elif n <= 9:
        return incremento(a, 20) / n
    elif n <= 12:
        return incremento(a, 30) / n