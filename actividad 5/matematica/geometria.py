def perCuad (a):
    return a * 4

def perRect (a, b):
    return a + a + b + b

def perTriang (a, b, c):
    return a + b + c

def perRombo (a):
    return a*4

def perParalel (a, b):
    return a + a + b + b

def perTrap (a, b, c, d):
    return a + b + c + d

def perPolig (a, n):
    return a * n

def perCirc (r):
    return 2*3.14*r

def areaCuad (a):
    return a * a

def areaRect (a, b):
    return a * b

def areaTriang (a, h):
    return (a * h) / 2

def areaRombo (d, c):
    return (d * c) / 2

def areaParalel (a, h):
    return a * h

def areaTrap (a, b, h):
    return ((a + b) / 2) * h

def areaPolig (a, n, apotema):
    return (perPolig(a, n) * apotema) / 2

def areaCirc (r):
    return 3.14 * r * r