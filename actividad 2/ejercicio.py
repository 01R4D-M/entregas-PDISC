import os

os.system("cls")

print("bienvenido".capitalize().center(40, "-"), "\n")

password = input("Ingrese su contraseña: ")

upper = False
lower = False
digit = False

for i in password:

    if i.isupper() == True: #verifico si la contraseña tiene mayusculas
        upper = True
    elif i.islower() == True: #verifico si la contraseña tiene minusculas
        lower = True
    elif i.isdigit() == True: #verifico si la contraseña tiene numeros
        digit = True

if len(password) >= 8: #verifico si la contraseña tiene como minimo 8 caracteres
    if upper and lower and digit: #verifico que la contraseña tenga tanto mayusculas como minusculas y numeros
        print("La contraseña es segura")
    else:
        print("La contraseña no es lo suficientemente segura")
else:
    print("La contraseña no es lo suficientemente larga")