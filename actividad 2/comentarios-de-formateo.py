variable = "a este texto se le aplicó la función capitalize()"
print(variable.capitalize(), "\n")

variable = "A ESTE TEXTO SE LE APLICÓ LA FUNCIÓN LOWER()"
print(variable.lower(), "\n")

variable = "a este texto se le aplicó la función upper()"
print(variable.upper(), "\n")

variable = "A este TEXTO se le APLICÓ la FUNCIÓN swapcase()"
print(variable.swapcase(), "\n")

variable = "a este texto se le aplicó la función title()"
print(variable.title(), "\n")

variable = "a este texto se le aplicó la función center()"
print(variable.center(65, "-"), "\n")

variable = "a este texto se le aplicó la función ljust()"
print(variable.ljust(65, "-"), "\n")

variable = "a este texto se le aplicó la función rjust()"
print(variable.rjust(65, "-"), "\n")

variable = "a este texto se le aplicó la función zfill()"
print(variable.zfill(65), "\n")

variable = "en la siguiente linea se aplica la función count() a este texto con la letra 'a'"
print(variable)
print(variable.count("a"), "\n")

variable = "en la siguiente linea se aplica la función find() a este texto con la palabra 'linea'"
print(variable)
print(variable.find("linea"), "\n")

variable = "en la siguiente linea se aplica la función startswith() a este texto con la palabra 'función'"
print(variable)
print(variable.startswith("función"), "\n")

variable = "en la siguiente linea se aplica la función endswith() con la palabra 'texto' a este texto"
print(variable)
print(variable.endswith("texto"), "\n")

variable = "en la siguiente linea se aplica la función isalnum() a este texto"
print(variable)
print(variable.isalnum(), "\n")

variable = "en la siguiente linea se aplica la función isalpha() a este texto"
print(variable)
print(variable.isalpha(), "\n")

variable = "en la siguiente linea se aplica la función islower() a este texto"
print(variable)
print(variable.islower(), "\n")

variable = "EN LA SIGUIENTE LINEA SE APLICA LA FUNCIÓN ISUPPER() A ESTE TEXTO"
print(variable)
print(variable.isupper(), "\n")

variable = "en la siguiente linea se aplica la función isspace() a este texto"
print(variable)
print(variable.isspace(), "\n")

variable = "en la siguiente linea se aplica la función istitle() a este texto"
print(variable)
print(variable.istitle(), "\n")

variable = "a{0}este{0}texto{0}se{0}le{0}aplicó{0}la{0}función{0}format(){0}para{0}imprimir{0}los{0}espacios"
print(variable.format(" "), "\n")

variable = "a+este+texto+se+le+aplicó+la+función+replace()+para+imprimir+los+espacios"
print(variable.replace("+", " "), "\n")

variable = "     a este texto se le aplicó la función strip() para eliminar los espacios a la derecha y a la izquierda     "
print(variable.strip(" "), "\n")

variable = "/////a este texto se le aplicó la función lstrip() para eliminar los caracteres a la izquierda"
print(variable.lstrip("/"), "\n")

variable = "a este texto se le aplicó la función rstrip() para eliminar los caracteres a la derecha$$$$$"
print(variable.rstrip("$"), "\n")

variable = "en la siguiente linea se aplica el operador in con la palabra 'la' en este texto"
print(variable)
print("la" in variable)